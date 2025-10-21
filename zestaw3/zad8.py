#!/user/bin/env python3

"""Dla dwóch sekwencji liczb lub znaków znaleźć:
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń)."""

s1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s2 = [2 * x for x in range(10)]

S1 = set(s1)
S2 = set(s2)

print(S1.intersection(S2))

print(S1.union(S2))
