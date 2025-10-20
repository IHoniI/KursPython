# ZADANIE 3.3
# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. Użyć pętli for lub while.

for i in range(31):
    if i%3 != 0:
        print(i)
