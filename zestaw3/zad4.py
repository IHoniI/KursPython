#!/user/bin/env python3

"""Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę."""

while True:
    x = input("liczba: ")
    if x == "stop":
        break
    try:
        xfloat = float(x)
        print(xfloat, "do potęgi 3 to: ", xfloat ** 3)
    except ValueError:
        print("Error, nie podano liczby float")
