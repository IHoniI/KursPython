import pytest
from rectangle import Rectangle
from points import Point


def test_init_invalid():
    with pytest.raises(ValueError, match="x1.*musi być mniejsze.*x2"):
        Rectangle(5, 0, 5, 3)

    with pytest.raises(ValueError, match="y1.*musi być mniejsze.*y2"):
        Rectangle(0, 5, 5, 5)


def test_str():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(1, 1, 5, 4)

    assert str(r1) == "[(0, 0), (4, 3)]"
    assert str(r2) == "[(1, 1), (5, 4)]"


def test_repr():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(1, 1, 5, 4)

    assert repr(r1) == "Rectangle(0, 0, 4, 3)"
    assert repr(r2) == "Rectangle(1, 1, 5, 4)"


def test_eq():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(0, 0, 4, 3)
    r3 = Rectangle(0, 0, 5, 3)

    assert r1 == r2
    assert not (r1 == r3)


def test_ne():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(0, 0, 5, 3)

    assert r1 != r2
    assert not (r1 != Rectangle(0, 0, 4, 3))


def test_from_points_basic():
    p1 = Point(0, 0)
    p2 = Point(4, 3)

    r = Rectangle.from_points((p1, p2))

    assert r.pt1.x == 0
    assert r.pt1.y == 0
    assert r.pt2.x == 4
    assert r.pt2.y == 3

    r = Rectangle.from_points([p1, p2])

    assert r == Rectangle(0, 0, 4, 3)


def test_from_points_wrong_count():
    p1 = Point(0, 0)

    with pytest.raises(ValueError, match="dokładnie 2 punkty"):
        Rectangle.from_points((p1,))

    with pytest.raises(ValueError, match="dokładnie 2 punkty"):
        Rectangle.from_points((p1, Point(1, 1), Point(2, 2)))


def test_from_points_not_point_objects():
    with pytest.raises(ValueError, match="obiektami Point"):
        Rectangle.from_points(((0, 0), (4, 3)))


def test_from_points_invalid_order():
    p1 = Point(5, 5)
    p2 = Point(0, 0)

    with pytest.raises(ValueError):
        Rectangle.from_points((p1, p2))


def test_coordinates():
    r = Rectangle(1, 2, 5, 7)

    assert r.left == 1
    assert r.right == 5
    assert r.bottom == 2
    assert r.top == 7


def test_dimensions():
    r = Rectangle(0, 0, 4, 3)

    assert r.width == 4
    assert r.height == 3


def test_corners():
    r = Rectangle(1, 2, 5, 7)

    assert r.topleft == Point(1, 7)
    assert r.topright == Point(5, 7)
    assert r.bottomleft == Point(1, 2)
    assert r.bottomright == Point(5, 2)


def test_center_property():
    r = Rectangle(0, 0, 4, 3)

    c = r.center
    assert c.x == 2
    assert c.y == 1.5


def test_area():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(1, 1, 5, 4)
    r3 = Rectangle(0, 0, 2, 2)
    r4 = Rectangle(10, 10, 20, 20)

    assert r1.area() == 12
    assert r2.area() == 12
    assert r3.area() == 4
    assert r4.area() == 100


def test_move():
    r1 = Rectangle(0, 0, 4, 3)

    moved = r1.move(1, 1)
    assert moved == Rectangle(1, 1, 5, 4)
    assert r1 == Rectangle(0, 0, 4, 3)

    moved2 = r1.move(-1, -1)
    assert moved2 == Rectangle(-1, -1, 3, 2)


def test_intersection_overlapping():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(1, 1, 5, 4)

    inter = r1.intersection(r2)
    assert inter == Rectangle(1, 1, 4, 3)


def test_intersection_identical():
    r1 = Rectangle(0, 0, 5, 5)
    r2 = Rectangle(0, 0, 5, 5)

    inter = r1.intersection(r2)
    assert inter == r1


def test_intersection_no_overlap():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(10, 10, 20, 20)

    with pytest.raises(ValueError):
        r1.intersection(r2)


def test_intersection_touching_edge():
    r1 = Rectangle(0, 0, 5, 5)
    r2 = Rectangle(5, 0, 10, 5)

    with pytest.raises(ValueError):
        r1.intersection(r2)


def test_cover_overlapping():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(1, 1, 5, 4)

    cover = r1.cover(r2)
    assert cover == Rectangle(0, 0, 5, 4)


def test_cover_disjoint():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(10, 10, 20, 20)

    cover = r1.cover(r2)
    assert cover == Rectangle(0, 0, 20, 20)


def test_cover_one_inside_other():
    r1 = Rectangle(0, 0, 4, 3)
    r2 = Rectangle(0, 0, 2, 2)

    cover = r1.cover(r2)
    assert cover == r1


def test_cover_identical():
    r1 = Rectangle(0, 0, 5, 5)
    r2 = Rectangle(0, 0, 5, 5)

    cover = r1.cover(r2)
    assert cover == r1


def test_make4_basic():
    r = Rectangle(0, 0, 4, 3)
    r1, r2, r3, r4 = r.make4()

    assert r1 == Rectangle(0, 1.5, 2, 3)
    assert r2 == Rectangle(2, 1.5, 4, 3)
    assert r3 == Rectangle(0, 0, 2, 1.5)
    assert r4 == Rectangle(2, 0, 4, 1.5)


def test_make4_square():
    r = Rectangle(0, 0, 2, 2)
    r1, r2, r3, r4 = r.make4()

    assert r1.area() == 1
    assert r2.area() == 1
    assert r3.area() == 1
    assert r4.area() == 1