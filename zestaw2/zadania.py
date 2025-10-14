# zadanie 2.10
# funkcja oblicza liczbę wyrazów w wieloliniowym stringu
def count_words(line):
    return len(line.split())


# zadanie 2.11
# funkcja wyswietlajaca string word tak,
# aby jego znaki byly rozdzielone znakiem podkreslenia
def special_print(word):
    print('_'.join(word))


# zadanie 2.12
# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line.
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.
def build_str(line):
    tmp = line.split()
    first = ''
    last = ''
    for i in range(len(tmp)):
        first += tmp[i][0]
        last += tmp[i][-1]

    print(first)
    print(last)




if __name__ == '__main__':
    lin = 'Podstawowe zdanie\nz , kilkoma\nlinijkami'
    print(count_words(lin))
    special_print("abc")
    build_str(lin)

