class Money:
    def __init__(self, amount):  
        self.__amount = amount

    def __eq__(self, other):
        return (self.__amount == other.__amount
                and self.__class__.__name__ == other.__class__.__name__)