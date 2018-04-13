import pytest
import datetime

from sssm.model.stock.common_stock import CommonStock
from sssm.model.stock.preferred_stock import PreferredStock
from sssm.model.trade.trade import Trade
from sssm.model.trade.type import TradeType
from sssm.storage import storage


def test_storage_get_trades():
    stock = CommonStock('TEA', 100)
    stock = storage.register_stock(stock)
    trades = storage.get_trades(stock)
    assert 0 == len(trades)
    storage.register_buy_trade(stock, 100, 100)
    trades = storage.get_trades(stock)
    assert 1 == len(trades)


def test_not_registered_stock():
    from sssm.storage.exceptions.stock_not_found_exception import StockNotFoundException
    with pytest.raises(StockNotFoundException):
        storage.get_trades(CommonStock('COLA', 100))


def test_get_trades():
    stock = CommonStock('WATER', 100)
    stock = storage.register_stock(stock)
    old_timestamp = datetime.datetime.now() - datetime.timedelta(minutes=100)
    old_trade = Trade(stock, TradeType.BUY, 100, 200)
    old_trade.timestamp = old_timestamp
    storage._trades[stock].append(old_trade)
    new_trade = storage.register_buy_trade(stock, 100, 150)

    trades = storage.get_trades(stock)
    assert 2 == len(trades)
    assert old_trade in trades
    assert new_trade in trades

    trades = storage.get_trades(stock, 15)
    assert 1 == len(trades)
    assert old_trade not in trades
    assert new_trade in trades


def test_get_last_dividend():
    stock = CommonStock('OIL', 100)
    stock = storage.register_stock(stock)
    from sssm.storage.exceptions.wrong_stock_type_dividend import WrongStockTypeDividend
    with pytest.raises(WrongStockTypeDividend):
        storage.register_preferred_dividend(stock, 8, 100, 100)
    old_dividend = storage.register_common_dividend(stock, 50)
    new_dividend = storage.register_common_dividend(stock, 55)
    dividend = storage.get_last_dividend(stock)
    assert old_dividend is not dividend
    assert new_dividend is dividend

    no_dividend_stock = PreferredStock('GAS', 100)
    no_dividend_stock = storage.register_stock(no_dividend_stock)
    dividend = storage.get_last_dividend(no_dividend_stock)
    assert dividend is None
