from testtools import TestCase
from example.money import Money, Sum
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

    def testPlusReturnsSum(self):
        five = Money.dollar(5)
        _sum = five.plus(five)
        self.assertEqual(five, _sum.augend)
        self.assertEqual(five, _sum.addend)

    def testReduceSum(self):
        _sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(_sum, "USD")
        self.assertEqual(Money.dollar(7), result)

    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def testReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def testIdentityRate(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))

    def testMixedAddition(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        self.assertEqual(Money.dollar(10), result)

    def testSumPlusMoney(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        _sum = Sum(fiveBucks, tenFrancs).plus(fiveBucks)
        result = bank.reduce(_sum, "USD")
        self.assertEqual(Money.dollar(15), result)

    def testSumTimes(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        _sum = Sum(fiveBucks, tenFrancs).times(2)
        result = bank.reduce(_sum, "USD")
        self.assertEqual(Money.dollar(20), result)