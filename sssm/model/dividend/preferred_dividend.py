from sssm.model.dividend.dividend import Dividend


class PreferredDividend(Dividend):
    def __init__(self, stock, last_dividend, fixed_dividend, par_value):
        super().__init__(stock, last_dividend)
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
