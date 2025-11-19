from math import gcd  # Py3


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return str(self.x) + "/" + str(self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac("+str(self.x) + ", " + str(self.y) + ")"

    def __cmp__(self, other):  # cmp(frac1, frac2)    # Py2
        num1 = self.x * other.y
        num2 = self.y * other.x
        if num2 == num1:
            return 0
        return 1 if num1 > num2 else -1

    def __eq__(self, other):
        if isinstance(other, Frac):
            num1 = self.x * other.y
            num2 = self.y * other.x
            return num2 == num1
        else:
            return self.x / self.y == other

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        num1 = self.x * other.y
        num2 = self.y * other.x
        return num1 < num2

    def __le__(self, other):
        num1 = self.x * other.y
        num2 = self.y * other.x
        return num1 <= num2

    # def __gt__(self, other): pass

    # def __ge__(self, other): pass

    def __add__(self, other):  # frac1 + frac2
        return Frac(
            self.x * other.y + other.x * self.y,
            self.y * other.y
        ).simplify()

    def __sub__(self, other):
        return Frac(
            self.x * other.y - other.x * self.y,
            self.y * other.y
        ).simplify()

    def __mul__(self, other):  # frac1 * frac2
        return Frac(
            self.x * other.x,
            self.y * other.y
        ).simplify()

    def __truediv__(self, other):  # frac1 / frac2, Py3
        n = self.x * other.y
        d = self.y * other.x

        if d == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")

        print(Frac(n, d))
        return Frac(n, d).simplify()

    __div__ = __truediv__

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs

    def simplify(self):
        if self.x < 0 and self.y < 0:
            x = -self.x
            y = -self.y
        elif self.x == 0:
            return Frac(0, 1)
        else:
            x = self.x
            y = self.y

        g = gcd(x, y)
        return Frac(x // g, y // g)

# Kod testujący moduł.

import unittest


class TestFrac(unittest.TestCase):
    def setUp(self) -> None:
        self.f1 = Frac(3, 4)
        self.f2 = Frac(1, 2)

    def test_print(self):  # test str() i repr()
        self.assertEqual(str(self.f1), "3/4")
        self.assertEqual(repr(self.f2), "Frac(1, 2)")

    def test_cmp(self):
        self.assertTrue(Frac(0, 3) == Frac(0, 2))
        self.assertTrue(Frac(0, 3) == Frac(0, -22))
        self.assertTrue(Frac(6, 3) == Frac(-12, -6))

        self.assertTrue(Frac(6, 4) != Frac(12, -6))
        self.assertTrue(Frac(9, 1) != Frac(1, 9))

        self.assertTrue(Frac(6, 4) > Frac(4, 6))
        self.assertTrue(Frac(1, 2) >= Frac(1, 2))

        self.assertTrue(Frac(-1, 2) < Frac(1, 2))
        self.assertTrue(Frac(1, 2) <= Frac(1, 2))
        self.assertFalse(Frac(6, 4) < Frac(4, 6))

    def test_simplify(self):
        self.assertEqual(Frac(2, 4).simplify(), Frac(1, 2))
        self.assertEqual(Frac(15, -5).simplify(), Frac(3, -1))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 2), Frac(1, 1))
        self.assertEqual(Frac(2, 5) + Frac(3, 15), Frac(3, 5))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 2), Frac(0, 1))
        self.assertEqual(self.f1 - self.f2, Frac(1, 4))

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Frac(3, 8))
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
        self.assertEqual(Frac(1, 3) / Frac(2, 9), Frac(3, 2))

    def test_float(self):
        self.assertEqual(Frac(1, 2), 0.5)
        self.assertEqual(float(Frac(1, 2)), 0.5)
