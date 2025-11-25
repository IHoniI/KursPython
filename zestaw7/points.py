import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""
    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):    # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points


# Kod testujący moduł.
class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.p0 = Point(0, 0)

    def test_print(self):  # test str() i repr()
        self.assertEqual(str(self.p0), "(0, 0)")
        self.assertEqual(repr(self.p0), "Point(0, 0)")

    def test_cmp(self):
        self.assertTrue(self.p0 == self.p0)
        self.assertFalse(self.p0 == Point(9, 7))
        self.assertFalse(Point(6, 6) == Point(1, 1))
        self.assertTrue(self.p0 != Point(9, 7))
        self.assertFalse(self.p0 != Point(0, 0))

    def test_add(self):
        self.assertEqual(self.p0 + self.p0, Point(0, 0))
        self.assertEqual(Point(3, 4) + Point(1, 2), Point(4, 6))

    def test_sub(self):
        self.assertEqual(self.p0 - self.p0, self.p0)
        self.assertEqual(Point(9, 8) - Point(5, 4), Point(4, 4))
        self.assertEqual(Point(0, 8) - Point(5, 4), Point(-5, 4))

    def test_mul(self):
        self.assertEqual(self.p0*self.p0, 0)
        self.assertEqual(Point(1, 2) * Point(2, 1), 4)

    def test_cross(self):
        self.assertEqual(self.p0.cross(Point(1, 2)), 0)
        self.assertEqual(Point(2, 1).cross(Point(1, 2)), 3)

    def test_length(self):
        self.assertEqual(self.p0.length(), 0)
        self.assertEqual(Point(3, 4).length(), 5)
