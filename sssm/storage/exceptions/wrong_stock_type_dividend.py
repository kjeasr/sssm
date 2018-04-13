class WrongStockTypeDividend(Exception):
    def __init__(self, expected, got):
        super().__init__('Expected: {}, got {}'.format(expected, got))
