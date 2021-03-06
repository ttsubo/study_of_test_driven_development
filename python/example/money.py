from example.expression import Expression

class Money(Expression):
    def __init__(self, amount, currency):  
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, other):
        return (self.__amount == other.__amount
                and self.currency() == other.currency())

    def times(self, multiplier):
        return Money(self.__amount * multiplier, self.__currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, toCurrency):
        rate = bank.rate(self.__currency, toCurrency)
        return Money(self.__amount / rate, toCurrency)

    def amount(self):
        return self.__amount

    def currency(self):
        return self.__currency

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
        amount = self.augend.reduce(bank, toCurrency).amount() + \
            self.addend.reduce(bank, toCurrency).amount()
        return Money(amount, toCurrency)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))