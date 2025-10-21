#!/user/bin/env python3

"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M)
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

# 1 sposob
symbols = ["I", "V", "X", "L", "C", "D", "M"]
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# 2 sposob
values = [1, 5, 10, 50, 100, 500, 1000]
d2 = dict.fromkeys(symbols)
for x in range(7): d2[symbols[x]] = values[x]

# 3 sposob
d3 = dict()
for x in range(7):
    d3[symbols[x]] = values[x]


def roman2int(roman):
    inti = 0

    symbols_index = 6
    while len(roman) > 0:
        if (n := roman.find(symbols[symbols_index])) == -1:
            symbols_index -= 1
        elif n == 0:
            inti += d[roman[0]]
            roman = roman[1:]
        else:
            # jesli liczba jest poprawna to n = 1
            inti += d[roman[1]] - d[roman[0]]
            roman = roman[n + 1:]

    print(inti)


r = "MMXXV"
r2 = "MMCDXLVII"
r3 = "XL"
roman2int(r2)
