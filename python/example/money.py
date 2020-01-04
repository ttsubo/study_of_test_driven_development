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

    def reduce(self, toCurrency):
        amount = self.augend.amount() + self.addend.amount()
        return Money(amount, toCurrency)