class Onkentes:
    def __init__(self, nev, ora, feladat):
        self.nev = nev
        self.ora = ora
        self.feladat = feladat

    def sok_ido(self):
        return self.ora >= 10
    
adatok = []

with open("./önkéntes kampány/onkentesek.txt", "r", encoding="utf-8") as f:
    next(f)
    next(f)
    for sorok in f:
        sor = sorok.strip().split(';')
        adat = {'nev':sor[0], 'ora':int(sor[1]), 'feladat':sor[2]}
        adatok.append(adat)

print(f'Az önkéntesek száma: {len(adatok)}')

a = 0
for adat in adatok:
    if adat['ora'] >= 10:
        a = a+1
print(f'10 vagy óránál többet dolgozott önkéntesek száma: {a}')

for adat in adatok:
    onkentes = Onkentes(adat['nev'], adat['ora'], adat['feladat'])
    o = onkentes.sok_ido()
    if o == True:
        print(f'{adat['nev']}, {adat['feladat']}')

with open("./önkéntes kampány/sokido.txt", "w", encoding="utf-8") as f2:
    for adat in adatok:
        onkentes = Onkentes(adat['nev'], adat['ora'], adat['feladat'])
        o = onkentes.sok_ido()
        if o == True:
            print(f'{adat['nev']}, {adat['feladat']}', file=f2)