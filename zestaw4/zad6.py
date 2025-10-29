"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną,
a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""


def sum_seq(sequence):
    if len(sequence) == 0:
        return 0
    elif isinstance(sequence[0], (list, tuple)):
        return sum_seq(sequence[0]) + sum_seq(sequence[1:])
    else:
        return sequence[0] + sum_seq(sequence[1:])


print(sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]))
assert sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]) == 45

print(sum_seq([1, [1, [1, (1, (1))]]]))
