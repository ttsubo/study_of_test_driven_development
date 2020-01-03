from testtools import TestCase
from example.dollar import Dollar

class MoneyTest(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)