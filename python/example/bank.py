class Bank():
    def __init__(self):
        self._rates = {}

    def reduce(self, source , toCurrency):
        return source.reduce(self, toCurrency)

    def add_rate(self, fromCurrency, toCurrency, rate):
        self._rates[(fromCurrency, toCurrency)] = rate

    def rate(self, fromCurrency, toCurrency):
        if fromCurrency == toCurrency:
            return 1
        return self._rates.get((fromCurrency, toCurrency))