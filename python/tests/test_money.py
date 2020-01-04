from testtools import TestCase
from example.money import Money
from example.bank import Bank

class MoneyTest(TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def testSimpleAddition(self):
        five = Money.dollar(5)
        _sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(_sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)