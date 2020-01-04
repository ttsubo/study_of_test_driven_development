from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, toCurrency):
        pass