from Calc import Calc
from unittest import TestCase


class TestMulit(TestCase):

    def testmulit(self):
        a = 10
        b = 6
        c = 60

        calc = Calc()
        lost = calc.multi(a, b)
        self.assertEqual(c, lost)

    def testmulit1(self):
        a = 5
        b = 6
        c = 30

        calc = Calc()
        lost = calc.multi(a, b)
        self.assertEqual(c, lost)

    def testmulit2(self):
        a = -10
        b = 6
        c = -60

        calc = Calc()
        lost = calc.multi(a, b)
        self.assertEqual(c, lost)

    def testmulit3(self):
        a = -10
        b = -6
        c = 60

        calc = Calc()
        lost = calc.multi(a, b)
        self.assertEqual(c, lost)