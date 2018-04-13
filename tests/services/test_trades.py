import pytest
import datetime

from sssm.model.stock.common_stock import CommonStock
from sssm.model.stock.preferred_stock import PreferredStock
import sssm.storage.storage
import sssm.services.trades

def test_volume_weight_stock_price():
    stock = CommonStock('GIN', 100)
    stock = sssm.storage.storage.register_stock(stock)
    sssm.storage.storage.register_buy_trade(stock, 10000, 100)
    sssm.storage.storage.register_buy_trade(stock, 5000, 110)
    sssm.storage.storage.register_sale_trade(stock, 2500, 105)
    vwsp = sssm.services.trades.volume_weight_stock_price(stock)
    assert 103.57 == round(vwsp, 2)


def test_GBCE():
    storage = sssm.storage.storage
    storage._stocks = {}
    storage._trades = {}
    storage._dividends = {}
    stocks = [
        ['TEA', 100],
        ['POP', 100],
        ['ALE', 125],
        ['JOE', 500]
    ]
    for stock in stocks:
        sssm.storage.storage.register_stock(CommonStock(stock[0], stock[1]))
    sssm.storage.storage.register_stock(PreferredStock('GIN', 100))
    index = sssm.services.trades.GBCE()
    assert 3.919 == round(index, 3)
    storage._stocks = {}
    storage._trades = {}
    storage._dividends = {}
