from abc import abstractmethod, ABCMeta


class Stock(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, ticker_symbol, price):
        self.ticker_symbol = ticker_symbol
        self.price = price
