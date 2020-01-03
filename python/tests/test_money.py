from testtools import TestCase
from example.dollar import Dollar

class MoneyTest(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))