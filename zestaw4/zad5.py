"""
Napisać funkcję odwracanie(L, left, right)
odwracającą kolejność elementów na liście od numeru left do right włącznie.
Lista jest modyfikowana w miejscu (in place).
Rozważyć wersję iteracyjną i rekurencyjną.
"""


def odwracanie_iter(L, left, right):
    while left != right:
        t = L[left]
        L[left] = L[right]
        L[right] = t

        left += 1
        right -= 1


def odwracanie_rek(L, left, right):
    if left == right:
        return L
    t = L[left]
    L[left] = L[right]
    L[right] = t
    return odwracanie_rek(L, left+1, right-1)


L = [1, 2, 3, 4, 5]
L2 = L.copy()
odwracanie_iter(L, 1, 3)
odwracanie_rek(L2, 1, 3)
print(L)
print(L2)

assert L == L2
