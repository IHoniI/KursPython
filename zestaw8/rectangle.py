from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2:
            raise ValueError(f"x1 ({x1}) musi być mniejsze od x2 ({x2})")
        if y1 >= y2:
            raise ValueError(f"y1 ({y1}) musi być mniejsze od y2 ({y2})")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({}, {}), ({}, {})]".format(
            self.pt1.x, self.pt1.y,
            self.pt2.x, self.pt2.y
        )

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(
            self.pt1.x, self.pt1.y,
            self.pt2.x, self.pt2.y
        )

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Należy podać dokładnie 2 punkty")

        p1, p2 = points

        if not all(isinstance(p, Point) for p in [p1, p2]):
            raise ValueError("Wszystkie elementy muszą być obiektami Point")

        return cls(p1.x, p1.y, p2.x, p2.y)

    @property
    def top(self):
        """Współrzędna y górnej krawędzi."""
        return self.pt2.y

    @property
    def bottom(self):
        """Współrzędna y dolnej krawędzi."""
        return self.pt1.y

    @property
    def left(self):
        """Współrzędna x lewej krawędzi."""
        return self.pt1.x

    @property
    def right(self):
        """Współrzędna x prawej krawędzi."""
        return self.pt2.x

    @property
    def width(self):
        """Szerokość prostokąta."""
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        """Wysokość prostokąta."""
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        """Lewy górny narożnik."""
        return Point(self.left, self.top)

    @property
    def topright(self):
        """Prawy górny narożnik."""
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        """Lewy dolny narożnik."""
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        """Prawy dolny narożnik."""
        return Point(self.right, self.bottom)

    @property
    def center(self):
        """Środek prostokąta."""
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        """Pole powierzchni."""
        return self.width * self.height

    def move(self, x, y):
        """Przesuniecie o (x, y)."""
        return Rectangle(
            self.pt1.x + x,
            self.pt1.y + y,
            self.pt2.x + x,
            self.pt2.y + y
        )

    def intersection(self, other):
        """Część wspólna prostokątów."""
        x1 = max(self.pt1.x, other.pt1.x)
        x2 = min(self.pt2.x, other.pt2.x)
        y1 = max(self.pt1.y, other.pt1.y)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Prostokąty nie mają części wspólnej")

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        """Prostąkąt nakrywający oba."""
        x1 = min(self.pt1.x, other.pt1.x)
        x2 = max(self.pt2.x, other.pt2.x)
        y1 = min(self.pt1.y, other.pt1.y)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2

        rect1 = Rectangle(self.pt1.x, cy, cx, self.pt2.y)
        rect2 = Rectangle(cx, cy, self.pt2.x, self.pt2.y)
        rect3 = Rectangle(self.pt1.x, self.pt1.y, cx, cy)
        rect4 = Rectangle(cx, self.pt1.y, self.pt2.x, cy)

        return (rect1, rect2, rect3, rect4)

