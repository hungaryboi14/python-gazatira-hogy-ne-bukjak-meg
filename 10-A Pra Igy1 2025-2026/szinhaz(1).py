def fizetendo(nev, db):
    return jegyek[nev] * db


jegyek = {}

with open("./szinhaz/darabok.txt", encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        if sor:
            nev, ar = sor.split(";")
            jegyek[nev] = int(ar)


jegy_nev = input("Melyik előadásra kér jegyet? ")
while jegy_nev not in jegyek:
    print("Hibás előadás név!")
    jegy_nev = input("Melyik előadásra kér jegyet? ")

db_input = input("Hány darabot? ")
while not db_input.isdigit() or int(db_input) <= 0:
    print("Hibás darabszám!")
    db_input = input("Hány darabot? ")
db = int(db_input)

osszeg = fizetendo(jegy_nev, db)
print(f"Fizetendő: {db} db {jegy_nev} = {osszeg} Ft")