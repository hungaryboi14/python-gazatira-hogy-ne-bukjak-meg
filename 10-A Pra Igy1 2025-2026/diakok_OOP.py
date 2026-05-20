class Tanulok:
    def __init__(self, nev, jegyek):
        self.nev = nev
        self.jegyek = jegyek

    def jegyek_kiir(self):
        print(f"Diák neve: {self.nev}, a diák jegyei: {self.jegyek}.")


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
