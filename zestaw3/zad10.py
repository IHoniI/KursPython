#!/user/bin/env python3

"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M)
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

symbols = ["I", "V", "X", "L", "C", "D", "M"]
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman2int(roman):

    inti = 0

    symbols_index = 6
    while len(roman) > 0:
        if (n := roman.find(symbols[symbols_index])) == -1:
            symbols_index -= 1
        elif n == 0:
            inti += d.get(roman[0])
            roman = roman[1:]

    print(inti)


r = "MMXXV"
roman2int(r)
