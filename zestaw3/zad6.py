#!/user/bin/env python3

"""
Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać.
Przykładowy prostokąt składający się 2 × 4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
"""


def create_rectangle(x, y):
    line1 = "---".join("+" for n in range(y))
    line2 = "   ".join("|" for n in range(y))+"\n"

    out = ""

    for i in range(x):
        out += line1 + "\n"
        out += line2

    out += line1

    return out


print(create_rectangle(4, 8))
