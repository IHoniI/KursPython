"""factorial(n)"""


def factorial(n):
    out = 1
    while n > 1:
        out *= n
        n -= 1

    return out


assert factorial(5) == 120

print(factorial(0))
