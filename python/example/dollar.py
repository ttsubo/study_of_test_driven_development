from example.money import Money

class Dollar(Money):
    def __init__(self, amount):  
        super(Dollar, self).__init__(amount)
        self.__amount = amount

    def times(self, multiplier):                                                    
        return Dollar(self.__amount * multiplier)