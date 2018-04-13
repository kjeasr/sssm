from sssm.model.stock.common_stock import CommonStock
from sssm.model.stock.preferred_stock import PreferredStock
import sssm.storage.storage
import sssm.services.dividend

def test_dividend_yield():
    preferred_stock = PreferredStock('TEST1', 100)
    storage = sssm.storage.storage
    dividend_service = sssm.services.dividend
    preferred_stock = storage.register_stock(preferred_stock)
    storage.register_preferred_dividend(preferred_stock, 8, .02, 100)
    standard_yield = dividend_service.dividend_yield(preferred_stock)
    new_price_yield = dividend_service.dividend_yield(preferred_stock, 105)
    assert standard_yield
    assert new_price_yield
    assert standard_yield != new_price_yield

    common_stock = CommonStock('TEST2', 105)
    common_stock = storage.register_stock(common_stock)
    storage.register_common_dividend(common_stock, 25)
    standard_yield = dividend_service.dividend_yield(common_stock)
    new_price_yield = dividend_service.dividend_yield(common_stock, 100)
    assert standard_yield
    assert new_price_yield
    assert standard_yield != new_price_yield


def test_p_e_ratio():
    common_stock = CommonStock('TEST3', 105)
    storage = sssm.storage.storage
    dividend_service = sssm.services.dividend
    common_stock = storage.register_stock(common_stock)
    storage.register_common_dividend(common_stock, 25)
    standard_yield = dividend_service.p_e_ratio(common_stock)
    new_price_yield = dividend_service.p_e_ratio(common_stock, 102)
    assert standard_yield
    assert new_price_yield
    assert standard_yield != new_price_yield