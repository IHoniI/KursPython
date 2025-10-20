#!/user/bin/env python3

"""Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
 Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
"""


def create_measure(length):
    line1 = "|"
    line2 = "0"

    for i in range(1, length+1):
        line1 += "....|"
        tmp = f"{i:>5}"
        line2 += tmp

    print(line1)
    print(line2)


create_measure(13)
