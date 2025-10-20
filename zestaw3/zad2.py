"""ZADANIE 3.2
Co jest złego w kodzie:"""

L = [3, 5, 4] ; L = L.sort()
print(L)
# ; jako oddzielenie instrukcji

#x, y = 1, 2, 3
# próbujemy przypisać 3 wartości do 2 zmiennych
# 3 będzie zignorowane

#X = 1, 2, 3 ; X[1] = 4
# ; oraz nie można przypisywać elementów do określonych miejsc w tuplach

#X = [1, 2, 3] ; X[3] = 4
# lista X ma 3 elementy więc index 3 zwraca "index out of range"

#X = "abc" ; X.append("d")
# X jest stringiem a nie listą. Nie można użyć append

L = list(map(pow, range(8)))
# pow potrzebuje 2 argumentów a dostaje tylko 1
# pokolei cyfry od 1 do 8 ale pojedynczo
