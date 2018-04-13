import datetime


class Trade:
    def __init__(self, stock, trade_type, quantity, price):
        self.stock = stock
        self.trade_type = trade_type
        self.price = price
        self.quantity = quantity
        self.timestamp = datetime.datetime.now()
