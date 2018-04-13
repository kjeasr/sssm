from sssm.model.dividend.dividend import Dividend


class CommonDividend(Dividend):
    def __init__(self, stock, last_dividend):
        super().__init__(stock, last_dividend)
