class Bank():
    def __init__(self):
        self._rates = {}

    def reduce(self, source , toCurrency):
        return source.reduce(self, toCurrency)

    def add_rate(self, fromCurrency, toCurrency, rate):
        target_rate = "{0}:{1}".format(fromCurrency, toCurrency)
        self._rates[target_rate] = rate

    def rate(self, fromCurrency, toCurrency):
        target_rate = "{0}:{1}".format(fromCurrency, toCurrency)
        if fromCurrency == toCurrency:
            return 1
        return self._rates.get(target_rate)