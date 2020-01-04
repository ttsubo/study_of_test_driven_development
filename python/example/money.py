from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount):  
        self.__amount = amount

    def __eq__(self, other):
        return (self.__amount == other.__amount
                and self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, multiplier):
        pass

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount)

    @classmethod
    def franc(cls, amount):
        return Franc(amount)


class Dollar(Money):
    def __init__(self, amount):  
        super(Dollar, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier):                                                    
        return Dollar(self.__amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super(Franc, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)