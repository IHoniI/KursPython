#!/user/bin/env python3

# zadanie 2.10
# funkcja oblicza liczbę wyrazów w wieloliniowym stringu
def count_words(line):
    return len(line.split())


# zadanie 2.11
# funkcja wyswietlajaca string word tak,
# aby jego znaki byly rozdzielone znakiem podkreslenia
def special_print(word):
    print('_'.join(word))


# zadanie 2.12, 2.13, 2.14, 2.15, 2.17
def line_operations(line):
    # Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line.
    # Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.
    words = line.split()
    first = ''
    last = ''
    for i in range(len(words)):
        first += words[i][0]
        last += words[i][-1]

    print(first)
    print(last)

    # 2.13 Znaleźć łączną długość wyrazów w stringu line.
    lenghts = [len(x) for x in words]
    print(sum(lenghts))

    # 2.14
    # (a) najdłuższy wyraz
    longest = max(line.split(), key=len)

    # (b) długość najdłuższego wyrazu
    length = len(longest)
    print("najdluzszy: "+ longest + ", dlugosc: " + str(length))

    # 2.17
    # alfabetycznie
    print("Alfabetycznie", sorted(words))
    # dlugoscowo
    print("Dlugoscowo", sorted(words, key=len))


# 2.16
# W tekście znajdującym się w stringu line zamienić ciąg znaków "GvR" na "Guido van Rossum"
def change_gvr(line):
    line = line.replace("GvR", "Guido van Rossum")
    print(line)


if __name__ == '__main__':
    lin = 'Podstawowe zdanie\nz GvR kilkoma\nlinijkami'
    print(count_words(lin))
    special_print("abc")
    line_operations(lin)
    change_gvr(lin)

    # 2.15
    L = [1,12,123,9]
    print(''.join(str(x) for x in L))

    # 2.18
    # policzyc zera
    number = 10020304050
    out18 = str(number).count("0")
    print(out18)

    # 2.19
    out19 = ''.join(str(x).zfill(3) for x in L)
    print(out19)
