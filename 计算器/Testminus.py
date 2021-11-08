from Calc import Calc
from unittest import TestCase


class TestMinus(TestCase):

    def testminus(self):
        a = 10
        b = 6
        c = 4

        calc = Calc()
        lost = calc.minus(a,b)
        self.assertEqual(c,lost)

    def testminus1(self):
        a = 5
        b = 6
        c = -1

        calc = Calc()
        lost = calc.minus(a, b)
        self.assertEqual(c, lost)

    def testminus2(self):
        a = -10
        b = 6
        c = -16

        calc = Calc()
        lost = calc.minus(a, b)
        self.assertEqual(c, lost)

    def testminus3(self):
        a = -10
        b = -6
        c = -4

        calc = Calc()
        lost = calc.minus(a, b)
        self.assertEqual(c, lost)

















