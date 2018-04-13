import datetime
from abc import abstractmethod


class Dividend:
    @abstractmethod
    def __init__(self, stock, last_dividend):
        self.stock = stock
        self.last_dividend = last_dividend
        self.timestamp = datetime.datetime.now()
