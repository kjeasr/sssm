from sssm.model.stock.stock import Stock


class CommonStock(Stock):

    def __init__(self, ticker_symbol, price):
        super().__init__(ticker_symbol, price)
