class Money():
    def __init__(self, amount, currency):  
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, other):
        return (self.__amount == other.__amount
                and self.currency() == other.currency())

    def times(self, multiplier):
        return Money(self.__amount * multiplier, self.__currency)

    def currency(self):
        return self.__currency

    @classmethod
    def dollar(cls, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")