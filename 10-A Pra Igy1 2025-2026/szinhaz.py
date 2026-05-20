def fizetendo(nev, db):
    return jegyek[nev] * db


jegyek = {}

with open("./szinhaz/darabok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        if sor:
            nev, ar = sor.split(";")
            jegyek[nev] = int(ar)


jegy_nev = input("Melyik előadásra kér jegyet? ")
while jegy_nev not in jegyek:
    print("Hibás előadás név!")
    jegy_nev = input("Melyik előadásra kér jegyet? ")

while True:
    try:
        db_input = int(input("Hány darabot? "))
        if db_input <= 0:
            print("Hibás darabszám!")
        else:
            break
    except ValueError:
        print("Hibás darabszám!")

osszeg = fizetendo(jegy_nev, db_input)
print(f"Fizetendő: {db_input} db {jegy_nev} = {osszeg} Ft")