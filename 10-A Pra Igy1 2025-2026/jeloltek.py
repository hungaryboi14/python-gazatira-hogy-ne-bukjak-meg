class Jelolt:
    def __init__(self, nev, osztaly, szavazat):
        self.nev = nev
        self.osztaly = osztaly
        self.szavazat = szavazat

    def elegseges(self):
        return self.szavazat >= 30
    
adatok = []
with open("./feladat4/jeloltek.txt", "r", encoding="utf-8") as fajl:
    next(fajl)
    next(fajl)
    for sorok in fajl:
        sor = sorok.strip().split(';')
        adat = {'nev':sor[0], 'osztaly':sor[1], 'szavazat':int(sor[2])}
        adatok.append(adat)

print(f'Összes jelölt száma: {len(adatok)}')


nevoszt = []
a = 0
for adat in adatok:
    elso = Jelolt(adat['nev'], adat['osztaly'], adat['szavazat'])
    if elso.elegseges() == True:
        asd = {'nev':adat['nev'], 'osztaly':adat['osztaly']}
        nevoszt.append(asd)
        a = a + 1
        print(f'30 szavazat felett kapott: {adat['nev']}, {adat['osztaly']}')
print(f'30 szavazat vagy 30 felett kaptak: {a} ')

with open("./feladat4/befutok.txt", "w", encoding="utf-8") as fajl2: 
    for adat in nevoszt:
        print('30 szavazat vagy 30 felett kapott: ', adat['nev'], ' ', adat['osztaly'], file=fajl2)