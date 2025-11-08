from math import gcd  # Py3


def add_frac(frac1, frac2):
    # frac1 + frac2
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    g = gcd(num, den)
    return [num // g, den // g]


def sub_frac(frac1, frac2):
    # frac1 - frac2
    num = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    g = gcd(num, den)
    return [num // g, den // g]


def mul_frac(frac1, frac2):
    # frac1 * frac2
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    g = gcd(num, den)
    return [num // g, den // g]


def div_frac(frac1, frac2):
    # frac1 / frac2
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    if den == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero!")
    g = gcd(num, den)
    return [num // g, den // g]


def is_positive(frac):  # bool, czy dodatni
    if (frac[0] >= 0 and frac[1] >= 0) or (frac[0] < 0 and frac[1] < 0):
        return True
    return False


def is_zero(frac):
    # bool, typu [0, x]
    if frac[0] == 0:
        return True
    return False

def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    num1 = frac1[0] * frac2[1]
    num2 = frac2[0] * frac1[1]
    if num2 == num1:
        return 0
    return 1 if num1 > num2 else -1


def frac2float(frac): # konwersja do float
    return frac[0]/frac[1]


# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [1, 3] #[3, 9]
        self.f2 = [2, 9]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac(self.f1, self.f2), [5, 9])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f1, self.f2), [1, 9])
        self.assertEqual(sub_frac([1, 2], [3, 5]), [-1, 10])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f1, self.f2), [2, 27])
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac(self.f1, self.f2), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([-21, -22]), True)
        self.assertEqual(is_positive(self.zero), True)
        self.assertEqual(is_positive([-4, 9]), 0)

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero(self.zero), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f1, self.f2), 1)
        self.assertEqual(cmp_frac([-4, 5], [4, -5]), 0)
        self.assertEqual(cmp_frac([7, 67], [67, 7]), -1)


    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertRaises(ZeroDivisionError, frac2float, [-5, 0])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
