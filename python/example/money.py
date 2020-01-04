from example.expression import Expression

class Money(Expression):
    def __init__(self, amount, currency):  
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self.amount == other.amount
                and self.currency() == other.currency())

    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, toCurrency):
        rate = bank.rate(self.currency(), toCurrency)
        return Money(self.amount / rate, toCurrency)

    def currency(self):
        return self._currency

    @classmethod
    def dollar(cls, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")

class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, toCurrency):
        amount = self.augend.reduce(bank, toCurrency).amount + \
            self.addend.reduce(bank, toCurrency).amount
        return Money(amount, toCurrency)

    def plus(self, addend):
        return Sum(self, addend)