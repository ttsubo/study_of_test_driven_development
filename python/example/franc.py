class Franc:
    def __init__(self, amount):  
        self.__amount = amount

    def __eq__(self, other):
        return self.__amount == other.__amount

    def times(self, multiplier):                                                    
        return Franc(self.__amount * multiplier)