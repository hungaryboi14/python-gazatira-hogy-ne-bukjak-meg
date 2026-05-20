def teljes(adatok):
    osszeg = 0
    for adat in adatok:
        osszeg = osszeg + adat["összeg"]
    return osszeg
adatok = []
with open('./feladat4/koltsegek.txt', 'r', encoding='utf-8') as koltseg:
    for sorok in koltseg:
        s = sorok.strip().split(';')
        adat = {'kategória':s[0], 'összeg':int(s[1])}
        adatok.append(adat)
asd = 0
while asd != 1:
    a = input("Adj meg egy kategóriát! ")
    for adat in adatok:
        if adat["kategória"] == a:
            asd = 1

k = 0
for adat in adatok:
    if adat['kategória'] == a:
        k = adat['összeg']
print(f'A {a} kategória összege: {k}')
print(teljes(adatok))

