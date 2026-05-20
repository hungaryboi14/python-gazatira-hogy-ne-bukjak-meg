class Foglalas:
    def __init__(self, nev, fo, idopont):
        self.nev = nev
        self.fo = fo
        self.idopont = idopont

    def nagy(self):
        return self.fo >= 6
    

adatok = []
with open("./feladat6/foglalasok.txt", "r", encoding="utf-8") as fajl:
    next(fajl)
    next(fajl)
    for sorok in fajl:
        sor = sorok.strip().split(';')
        foglalasok = {'név':sor[0], 'fő':int(sor[1]), 'időpont':(sor[2])}
        adatok.append(foglalasok)

print(f'{len(adatok)} db foglalás van beírva.')

a = 0
for adat in adatok:
    if adat['fő'] >= 6:
        a = a + 1
print(f'{a} nagy foglalás van beírva.')

with open("./feladat6/nagyok.txt", "w", encoding="utf-8") as file:
    for adat in adatok:
        foglalasok = Foglalas(adat['név'], adat['fő'], adat['időpont'])
        if foglalasok.nagy() == True:
            print(f'A nagy foglalás(ok)hoz tartozó név és időpont: {adat['név']}, {adat['időpont']}')
            print(f'A nagy foglalás(ok)hoz tartozó név és időpont: {adat['név']}, {adat['időpont']}', file=file)