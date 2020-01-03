from example.money import Money

class Franc(Money):
    def __init__(self, amount):  
        super(Franc, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier):                                                    
        return Franc(self.__amount * multiplier)