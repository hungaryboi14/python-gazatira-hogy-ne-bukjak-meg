class Beteg:
    def __init__(self, nev, kor, varakozas):
        self.nev = nev
        self.kor = kor
        self.varakozas = varakozas

    def sokat_vart(self):
        return self.varakozas >= 30
ad = []
with open("./python/vizitek/vizitek.txt", "r", encoding="utf-8") as f:
    next(f)
    next(f)
    for so in f:
        s = so.strip().split(";")
        a = {'név': s[0], 'kor': int(s[1]), 'várakozás': int(s[2])}
        ad.append(a)


print(f'{len(ad)} beteg érkezett')

k = []
asd = 0
for a in ad:
    k = Beteg(a['név'], a['kor'], a['várakozás'])
    if k.sokat_vart() == True:
        asd = asd + 1

print(f'{asd} beteg várt 30 percnél hosszabb ideig.')


with open("./python/vizitek/vartak.txt", "w", encoding="utf-8") as f2:
    asd = 0
    for a in ad:
        k = Beteg(a['név'], a['kor'], a['várakozás'])
        if k.sokat_vart() == True:
            asd = asd + 1
            print(f'{a['név']}, {a["kor"]}', file=f2)