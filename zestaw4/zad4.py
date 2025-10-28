"""fibo(n)"""


def fibo(n):
    n0 = 0
    n1 = 1
    out = 0

    for _ in range(n-1):
        out = n0 + n1
        n0 = n1
        n1 = out

    return out


print(fibo(7))
assert fibo(8) == 21
