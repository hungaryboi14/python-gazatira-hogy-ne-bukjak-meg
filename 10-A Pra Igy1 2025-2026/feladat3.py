import random


def paros(szamok, file="./iras/paros.txt"):
    with open(file, "w", encoding="utf-8") as paros:
        for szam in szamok:
            if szam % 2 == 0:
                paros.write(str(szam) + "\n")


def paratlan(szamok, file="./iras/paratlan.txt"):
    with open(file, "w", encoding="utf-8") as paratlan:
        for szam in szamok:
            if szam % 2 != 0:
                paratlan.write(str(szam) + "\n")


szamok = [random.randint(1, 50) for i in range(10)]


paros(szamok)
paratlan(szamok)

