import datetime

from sssm.model.trade.type import TradeType
from sssm.model.dividend.common_dividend import CommonDividend
from sssm.model.dividend.preferred_dividend import PreferredDividend
from sssm.model.stock.common_stock import CommonStock
from sssm.model.stock.preferred_stock import PreferredStock
from sssm.model.trade.trade import Trade

_stocks = {}

_trades = {}

_dividends = {}


def register_stock(stock):
    if stock.ticker_symbol not in _stocks:
        _stocks[stock.ticker_symbol] = stock
    else:
        stock = _stocks[stock.ticker_symbol]
    if stock not in _trades:
        _trades[stock] = []
    if stock not in _dividends:
        _dividends[stock] = []
    return stock


def get_stock(ticker_symbol):
    if ticker_symbol in _stocks:
        return _stocks[ticker_symbol]
    else:
        from sssm.storage.exceptions.stock_not_found_exception import StockNotFoundException
        raise StockNotFoundException()


def get_all_stocks():
    return _stocks.values()


def register_buy_trade(stock, quantity, price):
    return _register_trade(stock, TradeType.BUY, quantity, price)


def register_sale_trade(stock, quantity, price):
    return _register_trade(stock, TradeType.SALE, quantity, price)


def _register_trade(stock, trade_type, quantity, price):
    stock = get_stock(stock.ticker_symbol)
    _is_registered_stock(stock)
    trade = Trade(stock, trade_type, quantity, price)
    _trades[stock].append(trade)
    return trade


def get_trades(stock, minutes=None):
    stock = get_stock(stock.ticker_symbol)
    _is_registered_stock(stock)
    trades = _trades[stock]
    if minutes is not None:
        limit = datetime.datetime.now() - datetime.timedelta(minutes=minutes)
        trades = [trade for trade in trades if trade.timestamp >= limit]
    return trades


def register_common_dividend(stock, last_dividend):
    stock = get_stock(stock.ticker_symbol)
    _is_registered_stock(stock)
    _is_correct_stock_type_dividend(stock, CommonStock)
    dividend = CommonDividend(stock, last_dividend)
    _dividends[stock].append(dividend)
    return dividend


def register_preferred_dividend(stock, last_dividend, fixed_dividend, par_value):
    stock = get_stock(stock.ticker_symbol)
    _is_registered_stock(stock)
    _is_correct_stock_type_dividend(stock, PreferredStock)
    dividend = PreferredDividend(stock, last_dividend, fixed_dividend, par_value)
    _dividends[stock].append(dividend)
    return dividend


def get_last_dividend(stock):
    stock = get_stock(stock.ticker_symbol)
    _is_registered_stock(stock)
    dividends = _dividends[stock]
    dividends = sorted(dividends, key=lambda dividend: dividend.timestamp)
    if len(dividends) > 0:
        return dividends[-1]
    else:
        return None


# this is last line of defence to make sure that stock has been registered in all bases
def _is_registered_stock(stock):
    if (stock.ticker_symbol not in _stocks) or (stock not in _trades) or (stock not in _dividends):
        from sssm.storage.exceptions.stock_not_found_exception import StockNotFoundException
        raise StockNotFoundException()
    return True


def _is_correct_stock_type_dividend(stock, stock_cl):
    if not isinstance(stock, stock_cl):
        from sssm.storage.exceptions.wrong_stock_type_dividend import WrongStockTypeDividend
        raise WrongStockTypeDividend(stock_cl, stock.__class__.__name__)
