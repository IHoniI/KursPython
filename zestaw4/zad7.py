"""
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.

Napisać funkcję flatten(sequence),
która zwróci spłaszczoną listę wszystkich elementów sekwencji.

Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]
"""


def flatten(sequence: list) -> list:
    """zwraca splaszczona liste wszystkich elementow"""
    if len(sequence) == 0:
        return []
    elif isinstance(sequence[0], (list, tuple)):
        return flatten(sequence[0]) + flatten(sequence[1:])
    else:
        return [sequence[0]] + flatten(sequence[1:])


sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]


assert flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]) == [1,2,3,4,5,6,7,8,9]
