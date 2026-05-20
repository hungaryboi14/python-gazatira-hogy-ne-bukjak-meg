def ertek(termek, adatok):
    for adat in adatok:
        if adat['termék'] == termek:
            return adat['db'] * adat['ár']


adatok = []
with open("./feladat5/keszlet.txt", "r", encoding="utf-8") as fajl:
    for sorok in fajl:
        sor = sorok.strip().split(';')
        adat = {'termék':sor[0], 'db':int(sor[1]), 'ár':int(sor[2])}
        adatok.append(adat)

osszes = 0
for t in adatok:
    osszes = osszes + (t['db'] * t['ár'])
print(f'összes készletérték: {osszes}')

d = 0
while d != 1:
    termek = input(f"Add meg a termék nevét: ")
    for adat in adatok:
        if termek == adat['termék']:
            d = 1
            termekertek = ertek(termek, adatok)
    if d != 1:
        print(f"Nincs ilyen termék!")
print(f"A választott termék értéke: {termekertek}")