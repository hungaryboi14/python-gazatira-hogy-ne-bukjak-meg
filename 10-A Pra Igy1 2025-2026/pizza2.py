def fizetendo(nev, db):
    return pizzak[nev] * db


pizzak = {}

with open("./feladat6/pizzak.txt", encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        if sor:
            nev, ar = sor.split(";")
            pizzak[nev] = int(ar)


pizza_nev = input("Milyen pizzát kér? ")
while pizza_nev not in pizzak:
    print("Ismeretlen pizza!")
    pizza_nev = input("Milyen pizzát kér? ")


a = 0
while a != 1:
    try:
        db = int(input(f'Hány darabot? '))
        if db <= 0:
            a = 0
        else:
            a = 1
    except Exception as b:
        print(f'Valamit elírtál a hiba: {b}')

osszeg = fizetendo(pizza_nev, db)
print(f"Fizetendő: {db} db {pizza_nev} = {osszeg} Ft")