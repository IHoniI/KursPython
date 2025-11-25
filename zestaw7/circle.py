import math

from points import Point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        # pole powierzchni
        return math.pi * self.radius ** 2

    def move(self, x, y):
        # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if not isinstance(other, Circle):
            raise ValueError("other musi być okręgiem")

        if self.pt.distance(other.pt) + self.radius <= other.radius:
            # self zawiera sie w other
            return other
        elif self.pt.distance(other.pt) + other.radius <= self.radius:
            # other zawiera sie w self
            return self
        else:
            d = self.pt.distance(other.pt)
            r1 = self.radius
            r2 = other.radius

            t = (d + r2 - r1) / (2 * d)

            # Pozycja środka nowego okręgu:
            cx = self.pt.x + t * (other.pt.x - self.pt.x)
            cy = self.pt.y + t * (other.pt.y - self.pt.y)

            new_radius = t * d + r1

            return Circle(cx, cy, new_radius)


# Kod testujący moduł.
import unittest


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(0, 0, 5)
        self.c0 = Circle(1.2, 0.6, 5.34)
        self.c2 = Circle(0, 0, 3)
        self.c3 = Circle(-3, -4, 8)
        self.c4 = Circle(-3, -4, 60)

    def test_str(self):
        self.assertEqual(str(self.c1), "Circle(0, 0, 5)")
        self.assertEqual(str(self.c0), "Circle(1.2, 0.6, 5.34)")

    def test_cmp(self):
        self.assertTrue(self.c1 == Circle(0, 0, 5))
        self.assertFalse(self.c1 == Circle(0, 1, 5))
        self.assertTrue(self.c1 != Circle(0, 1, 5))

    def test_area(self):
        self.assertEqual(self.c1.area(), 78.53981633974483)
        self.assertEqual(self.c2.area(), 28.274333882308138)

    def test_move(self):
        self.assertEqual(self.c1.move(1, 1), Circle(1, 1, 5))
        self.assertEqual(self.c2.move(-10, 0), Circle(-10, 0, 3))

    def test_cover_contained(self):
        # self zawiera się w other
        c_small = Circle(1, 1, 1)
        c_big = Circle(0, 0, 5)
        self.assertEqual(c_small.cover(c_big), c_big)
        self.assertEqual(c_big.cover(c_small), c_big)

    def test_cover_identical(self):
        c1 = Circle(3, 4, 2)
        c2 = Circle(3, 4, 2)
        self.assertEqual(c1.cover(c2), c1)

    def test_cover_disjoint(self):
        # dwa okręgi rozłączne
        c1 = Circle(0, 0, 1)
        c2 = Circle(4, 0, 1)

        c = c1.cover(c2)

        # środek musi być na osi x i między 0 a 4
        self.assertAlmostEqual(c.pt.y, 0)
        self.assertGreater(c.pt.x, 0)
        self.assertLess(c.pt.x, 4)

        self.assertAlmostEqual(c.radius, 3)

    def test_cover_invalid_type(self):
        with self.assertRaises(ValueError):
            self.c1.cover("nie okrąg")
