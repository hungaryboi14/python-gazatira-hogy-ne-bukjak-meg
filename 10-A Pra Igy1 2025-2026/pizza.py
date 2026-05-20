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

db_input = input("Hány darabot? ")
while not db_input.isdigit() or int(db_input) <= 0:
    print("Hibás darabszám!")
    db_input = input("Hány darabot? ")
db = int(db_input)

osszeg = fizetendo(pizza_nev, db)
print(f"Fizetendő: {db} db {pizza_nev} = {osszeg} Ft")