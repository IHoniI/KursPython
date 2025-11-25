from itertools import cycle
import random


# 0 1 0 1 ...
def iter1():
    while True:
        yield 0
        yield 1


a = iter1()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print("###################################")

# zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
# [błądzenie przypadkowe na sieci kwadratowej 2D],

def random_steps():
    directions = ("N", "E", "S", "W")
    while True:
        yield random.choice(directions)


b = random_steps()
print(next(b))
print(next(b))
print(next(b))
print(next(b))

print("###################################")

# numery dni tygodnia

c = cycle([0, 1, 2, 3, 4, 5, 6])

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
