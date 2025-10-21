#!/user/bin/env python3

"""
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
spodziewany wynik [0,4,3,7,18].
"""

s = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

a = map(sum, s)
print(list(a))
