class Diak:
    def __init__(self, nev, kor, napok):
        self.nev = nev
        self.kor = kor
        self.napok = napok

    def marad(self):
        return self.napok >= 5

adatok = []
with open("./feladat5/diakok.txt", "r", encoding="utf-8") as fajl:
    next(fajl)
    next(fajl)
    for sorok in fajl:
        sor = sorok.strip().split(';')
        diak = {'nev':sor[0], 'kor':int(sor[1]), 'napok':int(sor[2])}
        adatok.append(diak)

print(f'{len(adatok)} diák jelentkezett')

a = 0
for adat in adatok:
    if adat['napok'] >= 5:
        a = a + 1
print(f'{a} diák marad 5 napnál többet')

with open("./feladat5/hosszabb.txt", "w", encoding="utf-8") as file:
    for adat in adatok:
        diak = Diak(adat['nev'], adat['kor'], adat['napok'])
        if diak.marad() == True:
            print(f'5 napnál tovább marad: {adat['nev']}, {adat['kor']}')
            print(f'5 napnál tovább marad: {adat['nev']}, {adat['kor']}', file=file)