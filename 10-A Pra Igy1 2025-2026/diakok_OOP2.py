class Tanulok:
    def __init__(self, nev, jegyek):
        self.nev = nev
        self.jegyek = [int(jegy) for jegy in jegyek.split(",")]

    def atlag(self):
        return sum(self.jegyek) / len(self.jegyek)

    def jegyek_kiir(self):
        print(f"Diák neve: {self.nev}, jegyei: {self.jegyek}, átlaga: {self.atlag()}")

    def eredmeny_kiir(self, szoveg):
        print(f"{szoveg} {self.nev}, {self.atlag()}")


diakok = []

with open("./OOP/Diakok.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        jegyek = adatok[1]
        diak = Tanulok(nev, jegyek)
        diakok.append(diak)

for diak in diakok:
    diak.jegyek_kiir()

legjobb = diakok[0]
legrosszabb = diakok[0]

for diak in diakok:
    if diak.atlag() > legjobb.atlag():
        legjobb = diak
    if diak.atlag() < legrosszabb.atlag():
        legrosszabb = diak

legjobb.eredmeny_kiir("Legjobb tanuló neve és átlaga:")
legrosszabb.eredmeny_kiir("Legrosszabb tanuló neve és átlaga:")

osszes_jegy = 0
osszes_db = 0

for diak in diakok:
    for jegy in diak.jegyek:
        osszes_jegy += jegy
        osszes_db += 1

osztaly_atlag = osszes_jegy / osszes_db

print(f"Az osztály átlaga: {osztaly_atlag}")