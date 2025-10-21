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
    line1 = "---".join("+" for n in range(y+1))
    line2 = "   ".join("|" for n in range(y+1))

    lines = line1+"\n"+line2
    out = "\n".join(lines for _ in range(x))

    out += "\n"+line1

    return out


print(create_rectangle(3, 5))
