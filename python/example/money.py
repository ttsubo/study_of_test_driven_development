from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):  
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, other):
        return (self.__amount == other.__amount
                and self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self.__currency

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Franc(amount, "CHF")


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        self.__amount = amount

    def times(self, multiplier):                                                    
        return Money.dollar(self.__amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        self.__amount = amount

    def times(self, multiplier):
        return Money.franc(self.__amount * multiplier)