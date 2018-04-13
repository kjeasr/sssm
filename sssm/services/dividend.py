from sssm.model.stock.common_stock import CommonStock
from sssm.model.stock.preferred_stock import PreferredStock
import sssm.storage.storage


def dividend_yield(stock, price=None):
    last_dividend = sssm.storage.storage.get_last_dividend(stock)
    if price is None:
        price = stock.price
    if isinstance(stock, CommonStock):
        return last_dividend.last_dividend / price
    if isinstance(stock, PreferredStock):
        return (last_dividend.fixed_dividend * last_dividend.par_value) / price


def p_e_ratio(stock, price=None):
    if price is None:
        price = stock.price
    last_dividend = sssm.storage.storage.get_last_dividend(stock)
    return price / last_dividend.last_dividend
