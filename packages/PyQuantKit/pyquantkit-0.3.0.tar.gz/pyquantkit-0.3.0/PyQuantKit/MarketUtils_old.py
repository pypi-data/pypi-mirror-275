from __future__ import annotations

import abc
import bisect
import datetime
import enum
import json
import math
import re
import warnings
from collections import defaultdict
from typing import overload, Iterable

import numpy as np
import pandas as pd

from . import LOGGER

LOGGER = LOGGER.getChild('MarketUtils')
__all__ = ['BarData', 'MarketData', 'OrderBook', 'TickData', 'TransactionData', 'TradeData', 'TransactionSide', 'TradeSide', 'get_data_attr', 'convert_to_bar']


class TransactionSide(enum.Enum):
    ShortOrder = AskOrder = Offer_to_Short = -3
    ShortOpen = Sell_to_Short = -2
    ShortFilled = LongClose = Sell_to_Unwind = ask = -1
    UNKNOWN = CANCEL = 0
    LongFilled = LongOpen = Buy_to_Long = bid = 1
    ShortClose = Buy_to_Cover = 2
    LongOrder = BidOrder = Bid_to_Long = 3

    def __lt__(self, other):
        warnings.warn(DeprecationWarning('Comparison of the <TransactionSide> deprecated!'))
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        warnings.warn(DeprecationWarning('Comparison of the <TransactionSide> deprecated!'))
        if self.__class__ is other.__class__:
            return self.value > other.value
        else:
            return self.value > other

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        else:
            return self.value == other

    def __neg__(self) -> TransactionSide:
        """
        return a opposite trade side, Long -> Short and Short -> Long
        :return: tr
        """
        if self is self.LongOpen:
            return self.LongClose
        elif self is self.LongClose:
            return self.LongOpen
        elif self is self.ShortOpen:
            return self.ShortClose
        elif self is self.ShortClose:
            return self.ShortOpen
        elif self is self.BidOrder:
            return self.AskOrder
        elif self is self.AskOrder:
            return self.BidOrder
        else:
            LOGGER.warning('No valid registered opposite trade side for {}'.format(self))
            return self.UNKNOWN

    def __hash__(self):
        return self.value

    @classmethod
    def from_offset(cls, direction: str, offset: str) -> TransactionSide:

        direction = direction.lower()
        offset = offset.lower()

        if direction in ['buy', 'long', 'b']:
            if offset in ['open', 'wind']:
                return cls.LongOpen
            elif offset in ['close', 'cover', 'unwind']:
                return cls.ShortOpen
            else:
                raise ValueError(f'Not recognized {direction} {offset}')
        elif direction in ['sell', 'short', 's']:
            if offset in ['open', 'wind']:
                return cls.ShortOpen
            elif offset in ['close', 'cover', 'unwind']:
                return cls.LongClose
            else:
                raise ValueError(f'Not recognized {direction} {offset}')
        else:
            raise ValueError(f'Not recognized {direction} {offset}')

    @classmethod
    def _missing_(cls, value: str | int):
        capital_str = str(value).capitalize()

        if capital_str == 'Long' or capital_str == 'Buy' or capital_str == 'B':
            trade_side = cls.LongOpen
        elif capital_str == 'Short' or capital_str == 'Ss':
            trade_side = cls.ShortOpen
        elif capital_str == 'Close' or capital_str == 'Sell' or capital_str == 'S':
            trade_side = cls.LongClose
        elif capital_str == 'Cover' or capital_str == 'Bc':
            trade_side = cls.ShortClose
        elif capital_str == 'Ask':
            trade_side = cls.AskOrder
        elif capital_str == 'Bid':
            trade_side = cls.BidOrder
        else:
            # noinspection PyBroadException
            try:
                trade_side = cls.__getitem__(value)
            except Exception as _:
                trade_side = cls.UNKNOWN
                LOGGER.warning('{} is not recognized, return TransactionSide.UNKNOWN'.format(value))

        return trade_side

    @property
    def sign(self) -> int:
        if self.value == self.Buy_to_Long.value or self.value == self.Buy_to_Cover.value:
            return 1
        elif self.value == self.Sell_to_Unwind.value or self.value == self.Sell_to_Short.value:
            return -1
        elif self.value == 0:
            return 0
        else:
            LOGGER.warning(f'Requesting .sign of {self.name} is not recommended, use .order_sign instead')
            return self.order_sign

    @property
    def order_sign(self) -> int:
        if self.value == self.LongOrder.value:
            return 1
        elif self.value == self.ShortOrder.value:
            return -1
        elif self.value == 0:
            return 0
        else:
            LOGGER.warning(f'Requesting .order_sign of {self.name} is not recommended, use .sign instead')
            return self.sign

    @property
    def offset(self) -> int:
        return self.sign

    @property
    def side_name(self):
        if self.value == self.Buy_to_Long.value or self.value == self.Buy_to_Cover.value:
            return 'Long'
        elif self.value == self.Sell_to_Unwind.value or self.value == self.Sell_to_Short.value:
            return 'Short'
        elif self.value == self.Offer_to_Short.value:
            return 'ask'
        elif self.value == self.Bid_to_Long.value:
            return 'bid'
        else:
            return 'Unknown'

    @property
    def offset_name(self):
        if self.value == self.Buy_to_Long.value or self.value == self.Sell_to_Short.value:
            return 'Open'
        elif self.value == self.Buy_to_Cover.value or self.value == self.Sell_to_Unwind.value:
            return 'Close'
        elif self.value == self.Offer_to_Short.value or self.value == self.Bid_to_Long.value:
            LOGGER.warning(f'Requesting offset of {self.name} is not supported, returns {self.side_name}')
            return self.side_name
        else:
            return 'Unknown'


TradeSide = TransactionSide


class MarketData(object):
    """
    Abstract parent class of BarData, TickData, TradeData and OrderBook
    """

    def __init__(self, ticker: str, timestamp: float):
        self.ticker = ticker
        self.timestamp = timestamp

    def __reduce__(self):
        return self.__class__.from_json, (self.to_json(),)

    def __hash__(self):
        return id(self)

    def __copy__(self):
        return self.__class__.from_json(self.to_json(fmt='dict'))

    def copy(self):
        return self.__copy__()

    @property
    @abc.abstractmethod
    def market_time(self) -> datetime.datetime | datetime.date | float | int:
        ...

    @property
    @abc.abstractmethod
    def market_price(self) -> float:
        ...

    @abc.abstractmethod
    def to_json(self, **kwargs) -> str:
        ...

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> MarketData:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.get('dtype', None)
        if dtype == 'BarData':
            return BarData.from_json(json_dict)
        elif dtype == 'TickData':
            return TickData.from_json(json_dict)
        elif dtype == 'TradeData':
            return TradeData.from_json(json_dict)
        elif dtype == 'OrderBook':
            return OrderBook.from_json(json_dict)
        else:
            raise TypeError(f'Invalid dtype {dtype}')

    @property
    def topic(self):
        return f'{self.ticker}.{self.__class__.__name__}'


class OrderBook(MarketData):
    class OrderBookEntry(object):

        """
        A OrderBook log Entry
        :param price: listed price
        :param volume: total listed volume at given price
        :param side: bid or ask
        """

        def __init__(
                self,
                price: float = 'nan',
                volume: float = 0.,
                side: TransactionSide | str | int = 0
        ):
            self.price = float(price)
            self.side = TransactionSide(side)
            self.volume = float(volume)

        @property
        def side_name(self) -> str:
            if self.side.order_sign > 0:
                return 'bid'
            else:
                return 'ask'

        def __lt__(self, other):
            if self.side.order_sign > 0:  # bid book
                if isinstance(other, self.__class__):
                    return self.price > other.price
                else:
                    return self.price > other
            else:  # ask book
                if isinstance(other, self.__class__):
                    return self.price < other.price
                else:
                    return self.price < other

        def __repr__(self):
            return f'<OrderBookEntry.{self.side_name.capitalize()}>({self.price:,.2f}: {self.volume:,.2f})'

        def __bool__(self):
            return self.volume > 0

    class Book(object):

        def __init__(self, side):
            self.side = TransactionSide(side)
            self._book: list[OrderBook.OrderBookEntry] = []
            self._dict: dict[float, OrderBook.OrderBookEntry] = {}

        def __iter__(self):
            self.sort()
            return sorted(self._book).__iter__()

        def __getitem__(self, item):
            if isinstance(item, int) and item not in self._dict:
                return self.at_level(item)
            elif isinstance(item, float):
                return self.at_price(item)
            else:
                raise KeyError(f'Ambiguous index value {item}, please use at_price or at_level specifically')

        def __contains__(self, price: float):
            return self._dict.__contains__(price)

        def __len__(self):
            return self._book.__len__()

        def __repr__(self):
            return f'<OrderBook.Book.{"Bid" if self.side > 0 else "Ask"}>[{", ".join([f"({entry.price:,.2f}: {entry.volume:,.2f})" for entry in self._book])}]'

        def __bool__(self):
            return bool(self._book) and all(self._book)

        def __sub__(self, other: OrderBook.Book) -> dict[float, float]:
            if not isinstance(other, self.__class__):
                raise TypeError(f'Expect type {self.__class__}, got {type(other)}')

            if self.side.order_sign != other.side.order_sign:
                raise ValueError(f'Expect side {self.side}, got {other.side}')

            diff = {}

            # bid book
            if (not self._dict) or (not other._dict):
                pass
            elif self.side.order_sign > 0:
                limit_0 = min(self._dict)
                limit_1 = min(other._dict)
                limit = max(limit_0, limit_1)
                contain_limit = True if limit_0 == limit_1 else False

                for _ in self:
                    price = _.price
                    volume = _.volume

                    if price > limit or (price >= limit and contain_limit):
                        diff[price] = volume

                for _ in other:
                    price = _.price
                    volume = _.volume

                    if price > limit or (price >= limit and contain_limit):
                        diff[price] = diff.get(price, 0.) - volume
            # ask book
            else:
                limit_0 = max(self._dict)
                limit_1 = max(other._dict)
                limit = min(limit_0, limit_1)
                contain_limit = True if limit_0 == limit_1 else False

                for _ in self:
                    price = _.price
                    volume = _.volume

                    if price < limit or (price <= limit and contain_limit):
                        diff[price] = volume

                for _ in other:
                    price = _.price
                    volume = _.volume

                    if price < limit or (price <= limit and contain_limit):
                        diff[price] = diff.get(price, 0.) - volume

            return diff

        def get(self, item=None, **kwargs) -> OrderBook.OrderBookEntry | None:
            if item is None:
                price = kwargs.pop('price', None)
                level = kwargs.pop('level', None)
            else:
                if isinstance(item, int):
                    price = None
                    level = item
                elif isinstance(item, float):
                    price = item
                    level = None
                else:
                    raise ValueError(f'Invalid type {type(item)}, must be int or float')

            if price is None and level is None:
                raise ValueError('Must assign either price or level in kwargs')
            elif price is None:
                try:
                    return self.at_level(level=level)
                except IndexError:
                    return None
            elif level is None:
                try:
                    return self.at_price(price=price)
                except KeyError:
                    return None
            else:
                raise ValueError('Must NOT assign both price or level in kwargs')

        def at_price(self, price: float):
            """
            get OrderBook.Book.Entry with specific price
            :param price: the given price
            :return: the logged OrderBook.Book.Entry
            """
            if price in self._dict:
                return self._dict.__getitem__(price)
            else:
                return None

        def at_level(self, level: int):
            """
            get OrderBook.Book.Entry with level num
            :param level: the given level
            :return: the logged OrderBook.Book.Entry
            """
            return self._book.__getitem__(level)

        def add(self, price: float, volume: float, **kwargs):
            self.add_entry(price=price, volume=volume)

        def add_entry(self, price: float, volume: float):
            entry = OrderBook.OrderBookEntry(price=price, volume=volume, side=self.side)
            bisect.insort(self._book, entry)
            if not math.isnan(price):
                self._dict[price] = entry
            return entry

        def update_entry(self, price: float, volume: float):
            if price in self._dict:
                if volume == 0:
                    self.pop(price=price)
                elif volume < 0:
                    LOGGER.warning(f'Invalid volume {volume}, expect a positive float.')
                    self.pop(price=price)
                else:
                    entry = self._dict[price]
                    entry.volume = volume
            else:
                self.add_entry(price=price, volume=volume)

        def append(self, entry: OrderBook.OrderBookEntry) -> None:
            if not isinstance(entry, OrderBook.OrderBookEntry):
                raise TypeError(f'Can only append [Entry] item to [Book], but received [{type(entry)}]')

            self._book.append(entry)

            if not math.isnan(entry.price):
                self._dict[entry.price] = entry

        def pop(self, price: float):
            entry = self._dict.pop(price, None)
            if entry is not None:
                self._book.remove(entry)
            else:
                raise KeyError(f'Price {price} not exist in order book')
            return entry

        def remove(self, entry: OrderBook.OrderBookEntry):
            try:
                self._book.remove(entry)
                self._dict.pop(entry.price)
            except ValueError:
                raise ValueError(f'Entry {entry} not exist in order book')

        def loc(self, prior: float = None, posterior: float = None):
            """
            loc transactions prior or posterior to given price. NOT COUNTING EQUAL!
            :param prior: the given price
            :param posterior: the given price
            :return: the summed transaction volume
            """
            volume = 0.
            if prior is None and posterior is None:
                raise ValueError('Must assign either prior or posterior in kwargs')
            elif posterior is None:
                for entry in self._book:
                    if entry.price > prior and self.side.order_sign > 0:
                        volume += entry.volume
                    elif entry.price < prior and self.side.order_sign < 0:
                        volume += entry.volume
            elif prior is None:
                for entry in self._book:
                    if entry.price < posterior and self.side.order_sign > 0:
                        volume += entry.volume
                    elif entry.price > posterior and self.side.order_sign < 0:
                        volume += entry.volume
            else:
                for entry in self._book:
                    if posterior > entry.price > prior and self.side.order_sign > 0:
                        volume += entry.volume
                    elif posterior < entry.price < prior and self.side.order_sign < 0:
                        volume += entry.volume

            return volume

        def refresh(self):
            _dict = {}
            _book = []

            for entry in self._book:
                if entry.volume == 0:
                    pass
                elif math.isnan(entry.price):
                    _book.append(entry)
                else:
                    _book.append(entry)
                    _dict[entry.price] = entry

            self._book = _book
            self._dict = _dict

        def sort(self):
            if self.side.order_sign > 0:
                self._book.sort(reverse=True, key=lambda x: x.price)
            else:
                self._book.sort(key=lambda x: x.price)

        @property
        def price(self):
            self.sort()
            return [entry.price for entry in self._book]

        @property
        def volume(self):
            self.sort()
            return [entry.volume for entry in self._book]

    def __init__(
            self, *,
            ticker: str,
            market_time: datetime.datetime = None,
            timestamp: float = None,
            bid: Book = None,
            ask: Book = None,
            **kwargs
    ):
        """
        MarketData object to store the snapshot of order book at given time
        :param ticker: the given ticker (symbol) of the trading asset
        :param market_time: the datetime of the snapshot
        :param bid: optional, a OrderBook.Book object store the order books at bid side. Recommend to input data with OrderBook.update() or OrderBook.Book.add() method
        :param ask: optional, a OrderBook.Book object store the order books at ask side
        :param kwargs: additional data send to OrderBook.update() method
        """
        super().__init__(
            ticker=ticker,
            timestamp=market_time.timestamp() if timestamp is None else timestamp
        )

        if bid is None:
            self.bid = self.Book(side=TransactionSide.BidOrder)
        elif isinstance(bid, self.__class__.Book):
            if bid.side == TransactionSide.BidOrder:
                self.bid = bid
            else:
                raise ValueError(f'Invalid OrderBook.bid.side, expect {TransactionSide.bid}, got {bid.side}')
        else:
            raise TypeError(f'Invalid OrderBook.bid, expect type {OrderBook.Book}, got {type(bid)}')

        if ask is None:
            self.ask = self.Book(side=TransactionSide.AskOrder)
        elif isinstance(ask, self.__class__.Book):
            if ask.side == TransactionSide.AskOrder:
                self.ask = ask
            else:
                raise ValueError(f'Invalid OrderBook.ask.side, expect {TransactionSide.ask}, got {ask.side}')
        else:
            raise TypeError(f'Invalid OrderBook.ask, expect type {OrderBook.Book}, got {type(ask)}')

        self.additional = {}
        self.update(**kwargs)

    def __call__(self, **kwargs):
        self.update(**kwargs)

    def __getattr__(self, item: str):
        if re.match('^((bid_)|(ask_))((price_)|(volume_))[0-9]+$', item):
            side = item.split('_')[0]
            key = item.split('_')[1]
            level = int(item.split('_')[2])
            book: 'OrderBook.Book' = self.__getattribute__(f'{side}')
            if 0 < level <= len(book):
                return book[level].__getattribute__(key)
            else:
                raise AttributeError(f'query level [{level}] exceed max level [{len(book)}]')
        else:
            raise AttributeError(f'{item} not found in {self.__class__}')

    def __getitem__(self, item):
        return self.__getattr__(item=item)

    def __setattr__(self, key, value):
        if re.match('^((bid_)|(ask_))((price_)|(volume_))[0-9]+$', key):
            self.update({key: value})
        else:
            super().__setattr__(key, value)

    def __repr__(self):
        return f'<OrderBook>([{self.market_time:%Y-%m-%d %H:%M:%S}] {self.ticker} {{Bid: [{", ".join([f"({entry.price:,.2f}: {entry.volume:,.2f})" for entry in self.bid])}], Ask: [{", ".join([f"({entry.price:,.2f}: {entry.volume:,.2f})" for entry in self.ask])}]}})'

    def __str__(self):
        return f'<OrderBook>([{self.market_time:%Y-%m-%d %H:%M:%S}] {self.ticker} {{Bid: {self.best_bid_price, self.best_bid_volume}, Ask: {self.best_ask_price, self.best_ask_volume}, Level: {self.max_level}}})'

    def __bool__(self):
        return bool(self.bid) and bool(self.ask)

    def __sub__(self, other: OrderBook):
        if not isinstance(other, self.__class__):
            raise TypeError(f'Expect type {self.__class__}, got {type(other)}')

        if self.ticker != other.ticker:
            raise ValueError(f'Expect ticker {self.ticker}, got {other.ticker}')

        if self.timestamp < other.timestamp:
            LOGGER.warning(f'Expect subtracted by newer order book, timestamp should >= {self.timestamp}, got {other.timestamp}')

        bid_diff = self.bid - other.bid
        ask_diff = self.ask - other.ask

        _ = OrderBookDiff(
            ticker=self.ticker,
            timestamp=other.timestamp,
            bid_diff=bid_diff,
            ask_diff=ask_diff
        )

        return _

    @overload
    def update(
            self,
            data: dict[str, float] = None,
            /,
            bid_price_1: float = math.nan,
            bid_volume_1: float = math.nan,
            ask_price_1: float = math.nan,
            ask_volume_1: float = math.nan,
            **kwargs: float
    ):
        ...

    def update(self, data: dict[str, float] = None, **kwargs):
        if not data:
            data = {}

        data.update(kwargs)

        if not data:
            LOGGER.debug(f'{self.__class__} has nothing to update, but still will purge the cache!')

        for name in data:
            if re.match('^((bid_)|(ask_))((price_)|(volume_))[0-9]+$', name):
                # validate data
                side = name.split('_')[0]
                key = name.split('_')[1]
                level = int(name.split('_')[2])
                value = data[name]
                book: OrderBook.Book = self.__getattribute__(f'{side}')

                if level <= 0:
                    raise ValueError(f'Level of name [{name}] must be greater than zero!')

                while level > len(book):
                    book.append(self.OrderBookEntry(price=np.nan))

                book.at_level(level - 1).__setattr__(key, value)
            else:
                self.additional[name] = data[name]
                LOGGER.warning(f'invalid name {name}, but still will store the data')

    def to_json(self, fmt='str', **kwargs) -> str | dict:
        data_dict = {
            'dtype': self.__class__.__name__,
            'ticker': self.ticker,
            'timestamp': self.timestamp,
            'bid': [(entry.price, entry.volume) for entry in self.bid],
            'ask': [(entry.price, entry.volume) for entry in self.ask],
        }

        if self.additional:
            data_dict['additional'] = self.additional

        if fmt == 'dict':
            return data_dict
        else:
            return json.dumps(data_dict, **kwargs)

    def get_book(self, side: TransactionSide, opposite=False) -> Book:
        """
        get corresponding order book. Buy -> bid book | Sell -> ask book
        :param side: the given trade side
        :param opposite: to return opposite book
        :return: a book
        """
        side_sign = side.sign

        if opposite:
            side_sign = -side_sign

        if side_sign > 0:
            return self.bid
        elif side_sign < 0:
            return self.ask
        else:
            raise ValueError(f'Invalid side {side}')

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> OrderBook:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.pop('dtype', None)
        if dtype is not None and dtype != cls.__name__:
            raise TypeError(f'Invalid dtype {dtype}')

        ticker = json_dict['ticker']
        timestamp = json_dict['timestamp']
        self = cls(ticker=ticker, timestamp=timestamp)

        for log in json_dict.pop('bid'):
            price = log[0]
            volume = log[1]
            self.bid.add_entry(price=price, volume=volume)

        for log in json_dict.pop('ask'):
            price = log[0]
            volume = log[1]
            self.ask.add_entry(price=price, volume=volume)

        self.additional.update(json_dict.get('additional', {}))

        return self

    @property
    def max_level(self) -> int:
        return max(len(self.bid), len(self.ask))

    @property
    def market_time(self):
        return datetime.datetime.fromtimestamp(self.timestamp)

    @property
    def market_price(self):
        """
        Mid-price for a order book snapshot
        :return: float
        """
        if np.isfinite(self.best_bid_price) and self.best_bid_price != 0 and np.isfinite(self.best_ask_price) and self.best_ask_price != 0:
            return (self.best_bid_price + self.best_ask_price) / 2
        else:
            return np.nan

    @property
    def mid_price(self):
        return self.market_price

    @property
    def spread(self):
        if np.isfinite(self.best_bid_price) and self.best_bid_price != 0 and np.isfinite(self.best_ask_price) and self.best_ask_price != 0:
            return self.best_ask_price - self.best_bid_price
        else:
            return np.nan

    @property
    def spread_pct(self):
        if np.isfinite(self.best_bid_price) and self.best_bid_price != 0 and np.isfinite(self.best_ask_price) and self.best_ask_price != 0:
            return (self.best_ask_price - self.best_bid_price) / self.mid_price
        else:
            return np.nan

    @property
    def best_bid_price(self):
        if self.bid.price:
            return self.bid.price[0]
        else:
            return np.nan

    @property
    def best_ask_price(self):
        if self.ask.price:
            return self.ask.price[0]
        else:
            return np.nan

    @property
    def best_bid_volume(self):
        if self.bid.volume:
            return self.bid.volume[0]
        else:
            return np.nan

    @property
    def best_ask_volume(self):
        if self.ask.volume:
            return self.ask.volume[0]
        else:
            return np.nan


class BarData(MarketData):
    def __init__(
            self, *,
            ticker: str,
            timestamp: float = None,  # the bar end timestamp
            bar_start_time: datetime.datetime | datetime.date,
            bar_span: datetime.timedelta,
            high_price: float = math.nan,
            low_price: float = math.nan,
            open_price: float = math.nan,
            close_price: float = math.nan,
            volume: float = 0.,
            notional: float = 0.,
            trade_count: int = 0,
            **kwargs
    ):
        """
        store bar data
        :param ticker: ticker (symbol) of the given asset (stock, future, option, crypto and etc.)
        :param high_price: max traded price of the given time frame
        :param low_price: min traded price of the given time frame
        :param open_price: trading price at the start of the bar
        :param close_price: trading price at the end of the bar
        :param bar_start_time: datetime.date for a daily bar or datetime.datetime for more detailed bar
        :param bar_span: the length of the given time frame
        :param volume: sum of traded volume at the given time frame
        :param notional: sum of traded notional, or turnover
        :param trade_count: number of trades happened during the time frame
        """

        if timestamp is None:
            if isinstance(bar_start_time, datetime.datetime):
                timestamp = (bar_start_time + bar_span).timestamp()
            else:
                LOGGER.warning('Auto-calculate timestamp of daily bar is not recommended')
                timestamp = datetime.datetime.combine(bar_start_time, datetime.time.max).timestamp()

        super().__init__(
            ticker=ticker,
            timestamp=timestamp
        )

        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.open_price = float(open_price)
        self.close_price = float(close_price)
        self.bar_start_time = bar_start_time
        self.bar_span = bar_span
        self.volume = float(volume)
        self.notional = float(notional)
        self.trade_count = int(trade_count)
        self.additional = {}

        self.additional.update(kwargs)

    def __repr__(self):
        return '<BarData>{}'.format(self.__dict__)

    def __eq__(self, other):
        if isinstance(other, BarData):
            return self.__repr__() == other.__repr__()
        else:
            return False

    def __lt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        assert other.bar_span == self.bar_span, 'BarSpan not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.bar_start_time < other.bar_start_time

    def __gt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        assert other.bar_span == self.bar_span, 'BarSpan not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.bar_start_time > other.bar_start_time

    def __le__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        assert other.bar_span == self.bar_span, 'BarSpan not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.bar_start_time <= other.bar_start_time

    def __ge__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        assert other.bar_span == self.bar_span, 'BarSpan not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.bar_start_time >= other.bar_start_time

    def __str__(self):
        if type(self.bar_start_time) is datetime.date:
            return f'<BarData>([{self.bar_start_time:%Y-%m-%d}] {self.ticker} Opened @ {self.open_price}; Closed @ {self.close_price}; Lasted {self.bar_span})'
        else:
            return f'<BarData>([{self.bar_start_time:%Y-%m-%d %H:%M:%S}] {self.ticker} Opened @ {self.open_price}; Closed @ {self.close_price}; Lasted {self.bar_span})'

    def to_json(self, fmt='str', **kwargs) -> str | dict:
        data_dict = {
            'dtype': self.__class__.__name__,
            'ticker': self.ticker,
            'market_time': (self.market_time.__class__.__name__, self.market_time.strftime('%Y-%m-%d %H:%M:%S')),
            'bar_span': self.bar_span.total_seconds(),
            'high_price': self.high_price,
            'low_price': self.low_price,
            'open_price': self.open_price,
            'close_price': self.close_price,
            'volume': self.volume,
            'notional': self.notional,
            'trade_count': self.trade_count
        }

        if self.additional:
            data_dict['additional'] = self.additional

        if fmt == 'dict':
            return data_dict
        else:
            return json.dumps(data_dict, **kwargs)

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> BarData:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.pop('dtype', None)
        if dtype is not None and dtype != cls.__name__:
            raise TypeError(f'Invalid dtype {dtype}')

        bar_start_time = json_dict.pop('market_time')

        self = cls(
            ticker=json_dict.pop('ticker'),
            high_price=json_dict.pop('high_price'),
            low_price=json_dict.pop('low_price'),
            open_price=json_dict.pop('open_price'),
            close_price=json_dict.pop('close_price'),
            bar_start_time=datetime.datetime.strptime(bar_start_time[1], '%Y-%m-%d %H:%M:%S'),
            bar_span=datetime.timedelta(seconds=json_dict.pop('bar_span')),
            volume=json_dict.pop('volume'),
            notional=json_dict.pop('notional'),
            trade_count=json_dict.pop('trade_count')
        )

        if bar_start_time[0] == 'date':
            self.bar_start_time = self.bar_start_time.date()

        self.additional.update(json_dict.get('additional', {}))

        return self

    # noinspection PyPep8Naming, SpellCheckingInspection
    @property
    def VWAP(self) -> float:
        if self.volume != 0:
            return self.notional / self.volume
        else:
            LOGGER.warning('[{}] {} Volume data not available, using close_price as default VWAP value'.format(self.bar_start_time, self.ticker))
            return self.close_price

    @property
    def is_valid(self, verbose=False) -> bool:
        try:
            assert type(self.ticker) is str, '{} Invalid ticker'.format(str(self))
            assert np.isfinite(self.high_price), '{} Invalid high_price'.format(str(self))
            assert np.isfinite(self.low_price), '{} Invalid low_price'.format(str(self))
            assert np.isfinite(self.open_price), '{} Invalid open_price'.format(str(self))
            assert np.isfinite(self.close_price), '{} Invalid close_price'.format(str(self))
            assert np.isfinite(self.volume), '{} Invalid volume'.format(str(self))
            assert np.isfinite(self.notional), '{} Invalid notional'.format(str(self))
            assert np.isfinite(self.trade_count), '{} Invalid trade_count'.format(str(self))
            assert isinstance(self.bar_start_time, (datetime.datetime, datetime.date)), '{} Invalid bar_start_time'.format(str(self))
            assert isinstance(self.bar_span, datetime.timedelta), '{} Invalid bar_span'.format(str(self))

            return True
        except AssertionError as e:
            if verbose:
                LOGGER.warning(str(e))
            return False

    @property
    def market_time(self):
        return self.bar_end_time

    @property
    def market_price(self):
        """
        close price for a BarData
        :return: float
        """
        return self.close_price

    @property
    def bar_type(self):
        if self.bar_span > datetime.timedelta(days=1):
            return 'Over-Daily'
        elif self.bar_span == datetime.timedelta(days=1):
            return 'Daily'
        elif self.bar_span > datetime.timedelta(hours=1):
            return 'Over-Hourly'
        elif self.bar_span == datetime.timedelta(hours=1):
            return 'Hourly'
        elif self.bar_span > datetime.timedelta(minutes=1):
            return 'Over-Minute'
        elif self.bar_span == datetime.timedelta(minutes=1):
            return 'Minute'
        else:
            return 'Sub-Minute'

    @property
    def bar_end_time(self):
        if self.bar_type == 'Daily':
            return self.bar_start_time
        else:
            return self.bar_start_time + self.bar_span


class TickData(MarketData):
    def __init__(
            self, *,
            ticker: str,
            last_price: float,
            market_time: datetime.datetime = None,
            timestamp: float = None,
            order_book: OrderBook = None,
            total_traded_volume: float = float('nan'),
            total_traded_notional: float = float('nan'),
            total_trade_count: int = 0,
            **kwargs
    ):
        """
        store tick data
        :param ticker: ticker (symbol) of the given asset (stock, future, option, crypto and etc.)
        :param market_time: datetime.datetime of the tick data
        :param last_price: last traded price
        :param total_traded_volume: total traded volume no after this tick, use float to compatible with crypto
        :param total_traded_notional: total traded notional no after this tick
        :param kwargs: additional OrderBook data
        :keyword bid_price: bid 1 price
        :keyword ask_price: ask 1 price
        :keyword bid_volume: bid 1 volume
        :keyword ask_volume: ask 1 volume
        """

        super().__init__(
            ticker=ticker,
            timestamp=market_time.timestamp() if timestamp is None else timestamp
        )

        if 'bid_price' in kwargs:
            kwargs['bid_price_1'] = kwargs.pop('bid_price')

        if 'ask_price' in kwargs:
            kwargs['ask_price_1'] = kwargs.pop('ask_price')

        if 'bid_volume' in kwargs:
            kwargs['bid_volume_1'] = kwargs.pop('bid_volume')

        if 'ask_volume' in kwargs:
            kwargs['ask_volume_1'] = kwargs.pop('ask_volume')

        if order_book is not None:
            self.order_book = order_book
        else:
            self.order_book = OrderBook(ticker=ticker, market_time=market_time, timestamp=timestamp)

        self.last_price = float(last_price)
        self.total_traded_volume = float(total_traded_volume)
        self.total_traded_notional = float(total_traded_notional)
        self.total_trade_count = int(total_trade_count)

        self.order_book.update(**kwargs)

    @property
    def market_time(self):
        return self.order_book.market_time

    @property
    def level_2(self):
        return self.order_book

    @property
    def bid_price(self):
        return self.order_book.best_bid_price

    @property
    def ask_price(self):
        return self.order_book.best_ask_price

    @property
    def bid_volume(self):
        return self.order_book.best_bid_volume

    @property
    def ask_volume(self):
        return self.order_book.best_ask_volume

    def __repr__(self):
        return '<TickData>{}'.format({key: item.__dict__ if key == 'level_2' else item for key, item in self.__dict__.items()})

    def __eq__(self, other):
        if isinstance(other, TickData):
            return self.__repr__() == other.__repr__()
        else:
            return False

    def __lt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time < other.market_time

    def __gt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time > other.market_time

    def __le__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time <= other.market_time

    def __ge__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time >= other.market_time

    def __str__(self):
        return f'<TickData>([{self.market_time:%Y-%m-%d %H:%M:%S}] {self.ticker} {{Bid: ({self.bid_price}: {self.bid_volume}), Ask: ({self.ask_price}: {self.ask_volume}), Last: {self.last_price}}})'

    def to_json(self, fmt='str', **kwargs) -> str | dict:
        data_dict = {
            'dtype': self.__class__.__name__,
            'ticker': self.ticker,
            'timestamp': self.timestamp,
            'last_price': self.last_price,
            'total_traded_volume': self.total_traded_volume,
            'total_traded_notional': self.total_traded_notional,
            'total_trade_count': self.total_trade_count,
            'bid': [(entry.price, entry.volume) for entry in self.order_book.bid],
            'ask': [(entry.price, entry.volume) for entry in self.order_book.ask],
        }

        if self.additional:
            data_dict['additional'] = self.additional

        if fmt == 'dict':
            return data_dict
        else:
            return json.dumps(data_dict, **kwargs)

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> TickData:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.pop('dtype', None)
        if dtype is not None and dtype != cls.__name__:
            raise TypeError(f'Invalid dtype {dtype}')

        ticker = json_dict.pop('ticker')
        timestamp = json_dict.pop('timestamp')
        order_book = OrderBook(ticker=ticker, timestamp=timestamp)

        for log in json_dict.pop('bid'):
            price = log[0]
            volume = log[1]
            order_book.bid.add_entry(price=price, volume=volume)

        for log in json_dict.pop('ask'):
            price = log[0]
            volume = log[1]
            order_book.ask.add_entry(price=price, volume=volume)

        self = cls(
            ticker=ticker,
            timestamp=timestamp,
            last_price=json_dict.pop('last_price'),
            order_book=order_book,
            total_traded_volume=json_dict.pop('total_traded_volume'),
            total_traded_notional=json_dict.pop('total_traded_notional'),
            total_trade_count=json_dict.pop('total_trade_count'),
        )

        self.additional.update(json_dict.get('additional', {}))

        return self

    @property
    def mid_price(self):
        return self.order_book.mid_price

    @property
    def market_price(self) -> float:
        """
        Last price for a TickData
        :return:
        """
        return self.last_price

    @property
    def additional(self):
        return self.order_book.additional


class TradeData(MarketData):
    def __init__(
            self, *,
            ticker: str,
            trade_price: float,
            trade_volume: float,
            trade_time: datetime.datetime = None,
            timestamp: float = None,
            side: int | float | str | TransactionSide = 0,
            multiplier: float = 1,
            notional: float = None,
            **kwargs
    ):
        """
        store trade data
        :param ticker: ticker (symbol) of the given asset (stock, future, option, crypto and etc.)
        :param trade_time: datetime.datetime of the trade
        :param trade_price: trade price
        :param trade_volume: use float to compatible with crypto
        :param side: TransactionSide indicating which side of the order book get taken
        :param multiplier: multiplier for contract trade data
        """

        super().__init__(
            ticker=ticker,
            timestamp=trade_time.timestamp() if timestamp is None else timestamp
        )

        self.price = float(trade_price)
        self.volume = float(trade_volume)
        self.trade_time = datetime.datetime.fromtimestamp(self.timestamp) if trade_time is None else trade_time
        self.side = TransactionSide(side)
        self.multiplier = float(multiplier)
        self.notional = self.price * self.volume * self.multiplier if notional is None else notional
        self.additional = {}

        self.additional.update(**kwargs)

    def __repr__(self):
        return '<TradeData>{}'.format({key: item.name if key == 'side' else item for key, item in self.__dict__.items()})

    def __eq__(self, other):
        if isinstance(other, TradeData):
            return self.__repr__() == other.__repr__()
        else:
            return False

    def __lt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.trade_time < other.trade_time

    def __gt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.trade_time > other.trade_time

    def __le__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.trade_time <= other.trade_time

    def __ge__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.trade_time >= other.trade_time

    def __str__(self):
        return '<TradeData>([{:%Y-%m-%d %H:%M:%S}] {} {} {:.2f} @ {:.2f} notional {:.2f})'.format(self.trade_time, self.ticker, self.side.name, self.volume, self.price, self.notional)

    def to_json(self, fmt='str', **kwargs) -> str | dict:

        data_dict = {
            'dtype': self.__class__.__name__,
            'ticker': self.ticker,
            'timestamp': self.timestamp,
            'side': self.side.value,
            'volume': self.volume,
            'price': self.price,

        }

        if self.multiplier != 1:
            data_dict['multiplier'] = self.multiplier

        if self.notional != self.price * self.volume * self.multiplier:
            data_dict['notional'] = self.notional

        if self.additional:
            data_dict['additional'] = self.additional

        if fmt == 'dict':
            return data_dict
        else:
            return json.dumps(data_dict, **kwargs)

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> TradeData:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.pop('dtype', None)
        if dtype is not None and dtype != cls.__name__:
            raise TypeError(f'Invalid dtype {dtype}')

        self = cls(
            ticker=json_dict.pop('ticker'),
            side=TransactionSide(json_dict.pop('side')),
            trade_volume=json_dict.pop('volume'),
            trade_price=json_dict.pop('price'),
            timestamp=json_dict.pop('timestamp'),
        )

        if 'multiplier' in json_dict:
            self.multiplier = json_dict['multiplier']

        if 'notional' in json_dict:
            self.notional = json_dict['notional']

        self.additional.update(json_dict.get('additional', {}))

        return self

    @staticmethod
    def merge(trade_data_list: list[TradeData]) -> TradeData | None:
        if not trade_data_list:
            return None

        ticker = trade_data_list[0].ticker
        assert all([trade.ticker == ticker for trade in trade_data_list]), 'input contains trade data of multiple ticker'
        timestamp = max([trade.timestamp for trade in trade_data_list])
        sum_volume = sum([trade.volume * trade.side.sign for trade in trade_data_list])
        sum_notional = sum([trade.notional * trade.side.sign for trade in trade_data_list])
        trade_side_sign = np.sign(sum_volume) if sum_volume != 0 else 1

        if sum_notional == 0:
            trade_price = 0
        else:
            trade_price = np.divide(sum_notional, sum_volume)

        trade_volume = sum_volume * trade_side_sign
        trade_side = TransactionSide(trade_side_sign)
        trade_notional = sum_notional * trade_side_sign

        merged_trade_data = TradeData(
            ticker=ticker,
            timestamp=timestamp,
            trade_price=trade_price,
            trade_volume=trade_volume,
            side=trade_side
        )
        merged_trade_data.notional = trade_notional

        return merged_trade_data

    @property
    def market_time(self):
        return self.trade_time

    @property
    def market_price(self) -> float:
        """
        Trade Price for a TradeData
        :return:
        """
        return self.price

    @property
    def flow(self):
        return self.side.sign * self.volume


class TransactionData(MarketData):
    def __init__(
            self, *,
            ticker: str,
            price: float,
            volume: float,
            transaction_time: datetime.datetime = None,
            timestamp: float = None,
            side: int | float | str | TransactionSide = 0,
            multiplier: float = 1,
            **kwargs
    ):
        """
        store trade data
        :param ticker: ticker (symbol) of the given asset (stock, future, option, crypto and etc.)
        :param trade_time: datetime.datetime of the trade
        :param trade_price: trade price
        :param trade_volume: use float to compatible with crypto
        :param side: TransactionSide indicating which side of the order book get taken
        :param multiplier: multiplier for contract trade data
        """

        super().__init__(
            ticker=ticker,
            timestamp=transaction_time.timestamp() if timestamp is None else timestamp
        )

        self.price = float(price)
        self.volume = float(volume)
        self.transaction_time = datetime.datetime.fromtimestamp(self.timestamp) if transaction_time is None else transaction_time
        self.side = TransactionSide(side)
        self.multiplier = float(multiplier)
        self.notional = self.price * self.volume * self.multiplier

        if transaction_time is None and timestamp is None:
            raise ValueError('Must assign ether transaction_time or timestamp')

        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        return '<TradeData>{}'.format({key: item.name if key == 'side' else item for key, item in self.__dict__.items()})

    def __eq__(self, other):
        if isinstance(other, TradeData):
            return self.__repr__() == other.__repr__()
        else:
            return False

    def __lt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time < other.market_time

    def __gt__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time > other.market_time

    def __le__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time <= other.market_time

    def __ge__(self, other):
        assert isinstance(other, self.__class__), 'Can not compare {} with {}'.format(other.__class__.__name__, self.__class__.__name__)
        assert other.ticker == self.ticker, 'Ticker not match! Can not compare TradeData of {} with {}'.format(other.ticker, self.ticker)
        return self.market_time >= other.market_time

    def __str__(self):
        return '<TransactionData>([{:%Y-%m-%d %H:%M:%S}] {} {} {:.2f} @ {:.2f} notional {:.2f})'.format(self.market_time, self.ticker, self.side.name, self.volume, self.price, self.notional)

    def to_json(self, fmt='str', **kwargs) -> str | dict:

        data_dict = {
            'dtype': self.__class__.__name__,
            'ticker': self.ticker,
            'timestamp': self.timestamp,
            'side': self.side.value
        }

        data_dict.update({key: value for key, value in self.__dict__.items() if key not in ['_ticker', 'side', 'timestamp']})

        if fmt == 'dict':
            return data_dict
        else:
            return json.dumps(data_dict, **kwargs)

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> TransactionData:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.pop('dtype', None)
        if dtype is not None and dtype != cls.__name__:
            raise TypeError(f'Invalid dtype {dtype}')

        self = cls(
            ticker=json_dict.pop('ticker'),
            side=TransactionSide(json_dict.pop('side')),
            volume=json_dict.pop('volume'),
            price=json_dict.pop('price'),
            timestamp=json_dict.pop('timestamp'),
        )

        for key, value in json_dict.items():
            setattr(self, key, value)

        return self

    @staticmethod
    def merge(trade_data_list: list[TransactionData]) -> TransactionData | None:
        if not trade_data_list:
            return None

        ticker = trade_data_list[0].ticker
        assert all([trade.ticker == ticker for trade in trade_data_list]), 'input contains trade data of multiple ticker'
        trade_time = max([trade.market_time for trade in trade_data_list])
        sum_volume = sum([trade.volume * trade.side.sign for trade in trade_data_list])
        sum_notional = sum([trade.notional * trade.side.sign for trade in trade_data_list])
        trade_side_sign = np.sign(sum_volume) if sum_volume != 0 else 1

        if sum_notional == 0:
            trade_price = 0
        else:
            trade_price = np.divide(sum_notional, sum_volume)

        trade_volume = sum_volume * trade_side_sign
        trade_side = TransactionSide(trade_side_sign)
        trade_notional = sum_notional * trade_side_sign

        merged_trade_data = TransactionData(
            ticker=ticker,
            market_time=trade_time,
            price=trade_price,
            volume=trade_volume,
            side=trade_side
        )
        merged_trade_data.notional = trade_notional

        return merged_trade_data

    @property
    def market_time(self):
        if self.transaction_time:
            return self.transaction_time
        else:
            return datetime.datetime.fromtimestamp(self.timestamp)

    @property
    def market_price(self) -> float:
        """
        Trade Price for a TradeData
        :return:
        """
        return self.price

    @property
    def flow(self):
        return self.side.sign * self.volume


class OrderBookDiff(MarketData):
    def __init__(
            self,
            ticker: str,
            market_time: datetime.datetime = None,
            timestamp: float = None,
            bid_diff=None,
            ask_diff=None,
            **kwargs):

        super().__init__(
            ticker=ticker,
            timestamp=market_time.timestamp() if timestamp is None else timestamp
        )

        self.bid_diff = {} if bid_diff is None else dict(bid_diff)
        self.ask_diff = {} if ask_diff is None else dict(ask_diff)

        self.additional = dict(**kwargs)

    def __repr__(self):
        return f'<OrderBookDiff>{self.ticker}'

    def __str__(self):
        return f'<OrderBookDiff>([{self.market_time:%Y-%m-%d %H:%M:%S}] {self.ticker} with {len(self.bid_diff) + len(self.ask_diff)} diffs)'

    def to_json(self, fmt='str', **kwargs) -> str | dict:

        data_dict = {
            'dtype': self.__class__.__name__,
            'ticker': self.ticker,
            'timestamp': self.timestamp,
            'bid_diff': self.bid_diff,
            'ask_diff': self.ask_diff,
        }

        if self.additional:
            data_dict['additional'] = self.additional

        if fmt == 'dict':
            return data_dict
        else:
            return json.dumps(data_dict, **kwargs)

    @classmethod
    def from_json(cls, json_message: str | bytes | bytearray | dict) -> OrderBookDiff:
        if isinstance(json_message, dict):
            json_dict = json_message
        else:
            json_dict = json.loads(json_message)

        dtype = json_dict.pop('dtype', None)
        if dtype is not None and dtype != cls.__name__:
            raise TypeError(f'Invalid dtype {dtype}')

        self = cls(
            ticker=json_dict.pop('ticker'),
            timestamp=json_dict.pop('timestamp'),
            bid_diff=json_dict.pop('bid_diff'),
            ask_diff=json_dict.pop('ask_diff'),
            **json_dict.get('additional', {})
        )

        return self

    @property
    def market_time(self):
        return datetime.datetime.fromtimestamp(self.timestamp)

    @property
    def market_price(self) -> float:
        return np.nan


def get_data_attr(
        data: list[MarketData] | dict[str, dict[datetime.datetime | datetime.date, MarketData] | list[MarketData]] = None,
        key: str = 'close_price',
        **kwargs
) -> pd.DataFrame | pd.Series:
    """
    convert a dict[symbol, List[MarketData] or dict[symbol, MarketData]] dictionary to pandas data frame by a certain key(name)
    :param data: dict of list of input MarketData
    :param key: the key(name) to extract from
    :return: a pandas DataFrame or pandas Series
    """
    historical_data = kwargs.pop('historical_data', None)
    if historical_data is not None:
        LOGGER.warning(DeprecationWarning('arg [historical_data] deprecated, use arg [data] instead'))
        data = historical_data

    data_dict = defaultdict(dict)

    if isinstance(data, dict):
        for ticker in data.keys():
            if isinstance(data[ticker], dict):
                market_data_list = data[ticker].values()
            elif isinstance(data[ticker], Iterable):
                market_data_list = data[ticker]
            else:
                raise TypeError(f'Invalid data Type {type(data[ticker])}')

            for market_data in market_data_list:
                data_dict[market_data.ticker][market_data.market_time] = getattr(market_data, key, float('nan'))
    elif isinstance(data, Iterable):
        for market_data in data:
            data_dict[market_data.ticker][market_data.market_time] = getattr(market_data, key, float('nan'))
    else:
        raise TypeError(f'Invalid data Type {type(data)}')

    result = pd.DataFrame(data_dict).sort_index(ascending=True)

    if len(result.columns) == 1:
        return result.iloc[:, 0]
    else:
        return result


def data_alignment(*args, **kwargs):
    return get_data_attr(*args, **kwargs)


def convert_to_bar(
        data_sequence: dict[datetime.datetime, MarketData] | list[MarketData],
        **kwargs,
) -> dict[datetime.datetime, BarData]:
    """
    Convert tick / trade / bar data list or dict to bar data with given interval
    :param data_sequence: dictionary or list of market data, DO NOT PASS A NEST DICT
    :keyword bar_span: bar_span in timedelta, fallback to interval if not given
    :keyword interval: bar_span in seconds, default = 60
    :keyword trading_hour_checker: a check function return whether the given datetime is in trading hour. Use CN-A stock trading hour by default
    :return: a dictionary with key = bar start time, value = minute bar data
    """

    if isinstance(data_sequence, dict):
        market_data_list = list(data_sequence.values())
    elif isinstance(data_sequence, list):
        market_data_list = data_sequence
    else:
        raise Exception('Invalid data type')

    if 'trading_hour_checker' not in kwargs:
        def default_checker(mt):
            if mt.time() < datetime.time(hour=9, minute=30) \
                    or datetime.time(hour=11, minute=30) <= mt.time() < datetime.time(hour=13, minute=00) \
                    or mt.time() >= datetime.time(hour=15, minute=00):
                return False
            else:
                return True

        trading_hour_checker = default_checker
    else:
        trading_hour_checker = kwargs['trading_hour_checker']

    bar_data_dict = {}

    market_data_list.sort(key=lambda x: x.market_time)
    last_tick_total_volume = 0.0
    last_tick_total_notional = 0.0
    last_tick_total_trades = 0

    if 'bar_span' in kwargs:
        bar_span = kwargs['bar_span']
    else:
        bar_span = datetime.timedelta(seconds=kwargs.get('interval', 60))

    last_bar_start_time = None

    bar_data = None
    for market_data in market_data_list:  # type: MarketData
        # if market data is not in active hours
        if trading_hour_checker is not None and not trading_hour_checker(market_data.market_time):
            if isinstance(market_data, TickData):
                last_tick_total_volume = market_data.total_traded_volume
                last_tick_total_notional = market_data.total_traded_notional
                last_tick_total_trades = market_data.total_trade_count

            continue
        # with active bar data
        if bar_data is not None:
            # next trading day
            if market_data.market_time.date() > bar_data.bar_start_time.date():
                last_tick_total_volume = 0.0
                last_tick_total_notional = 0.0
                last_tick_total_trades = 0
                last_bar_start_time = None
                bar_data_dict[bar_data.bar_start_time] = bar_data
            # next bar
            if market_data.market_time > bar_data.bar_start_time + bar_span:
                last_bar_start_time = bar_data.bar_start_time
                bar_data_dict[bar_data.bar_start_time] = bar_data
                bar_data = None
            # current bar
            else:
                bar_data.high_price = max(bar_data.high_price, market_data.market_price)
                bar_data.low_price = min(bar_data.low_price, market_data.market_price)
                bar_data.close_price = market_data.market_price
                if isinstance(market_data, TickData):
                    bar_data.volume += market_data.total_traded_volume - last_tick_total_volume
                    bar_data.notional += market_data.total_traded_notional - last_tick_total_notional
                    bar_data.trade_count += market_data.total_trade_count - last_tick_total_trades

                    last_tick_total_volume = market_data.total_traded_volume
                    last_tick_total_notional = market_data.total_traded_notional
                    last_tick_total_trades = market_data.total_trade_count
                elif isinstance(market_data, TradeData):
                    bar_data.volume += market_data.volume
                    bar_data.notional += market_data.notional
                    bar_data.trade_count += 1
                elif isinstance(market_data, BarData):
                    bar_data.volume += market_data.volume
                    bar_data.notional += market_data.notional
                    bar_data.trade_count += market_data.trade_count
                else:
                    pass

                if market_data.market_time == bar_data.bar_start_time + bar_span:
                    last_bar_start_time = bar_data.bar_start_time
                    bar_data_dict[bar_data.bar_start_time] = bar_data
                    bar_data = None

        if bar_data is None:
            if last_bar_start_time is None:
                bar_start_time = datetime.datetime(
                    market_data.market_time.year,
                    market_data.market_time.month,
                    market_data.market_time.day,
                    market_data.market_time.hour,
                    market_data.market_time.minute
                )
            else:
                i = (market_data.market_time - last_bar_start_time) // bar_span
                bar_start_time = last_bar_start_time + i * bar_span

            bar_data = BarData(
                ticker=market_data.ticker,
                high_price=market_data.market_price,
                low_price=market_data.market_price,
                open_price=market_data.market_price,
                close_price=market_data.market_price,
                bar_start_time=bar_start_time,
                bar_span=bar_span,
            )

            if isinstance(market_data, TickData):
                bar_data.volume = market_data.total_traded_volume - last_tick_total_volume
                bar_data.notional = market_data.total_traded_notional - last_tick_total_notional
                bar_data.trade_count = market_data.total_trade_count - last_tick_total_trades

                last_tick_total_volume = market_data.total_traded_volume
                last_tick_total_notional = market_data.total_traded_notional
                last_tick_total_trades = market_data.total_trade_count
            elif isinstance(market_data, TradeData):
                bar_data.volume = market_data.volume
                bar_data.notional = market_data.notional
                bar_data.trade_count = 1
            elif isinstance(market_data, BarData):
                bar_data.volume = market_data.volume
                bar_data.notional = market_data.notional
                bar_data.trade_count = market_data.trade_count
            else:
                pass

    return bar_data_dict
