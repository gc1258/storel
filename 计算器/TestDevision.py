from Calc import Calc
from unittest import TestCase


class TestDevision(TestCase):

    def testdevision(self):
        a = 60
        b = 6
        c = 10

        calc = Calc()
        lost = calc.devision(a, b)
        self.assertEqual(c, lost)

    def testdevision1(self):
        a = 20
        b = 3
        c = 6.66

        calc = Calc()
        lost = calc.devision(a, b)
        self.assertEqual(c, lost)

    def testdevision2(self):
        a = 10
        b = 2
        c = 5

        calc = Calc()
        lost = calc.devision(a, b)
        self.assertEqual(c, lost)

    def testdevision3(self):
        a = 2
        b = 10
        c = 0.2

        calc = Calc()
        lost = calc.devision(a, b)
        self.assertEqual(c, lost)