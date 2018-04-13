import sssm.storage.storage


def volume_weight_stock_price(stock):
    trades = sssm.storage.storage.get_trades(stock, 15)
    pq = 0
    q = 0
    for trade in trades:
        pq = pq + (trade.price * trade.quantity)
        q = q + trade.quantity
    return pq / q


def GBCE():
    stocks = sssm.storage.storage.get_all_stocks()
    sum_of_prices = sum([stock.price for stock in stocks])
    return sum_of_prices**(len(stocks) **-1)
