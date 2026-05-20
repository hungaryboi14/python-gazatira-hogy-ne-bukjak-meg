asd = []

with open('./munkasok/munkasok.txt', "r", encoding="utf-8") as fajl:
    next(fajl)
    for sorok in fajl:
        s = sorok.strip().split(';')
        dsa = {'Név': s[0], 'Életkor': s[1], 'Fizetés': int(s[2])}
        asd.append(dsa)

print(f'Összes munkás adatai:')

for dsa in asd:
    print(f'Név: {dsa['Név']}, Életkor: {dsa['Életkor']}, Fizetés: {dsa['Fizetés']}')
hgf = []
a=0

for dsa in asd:
    if dsa['Fizetés'] >= 500000:
        a = a+1
        hgf.append(dsa)


print("\n" + f'500 000 Ft felett keresők száma: {a}' + "\n")

print("Eredmények elmentve az 'eredmenyek.txt' fájlba.")

with open("./munkasok/eredmenyek.txt", "w", encoding="utf-8") as f:
    print(f'Munkások, akik 500 000 Ft felett keresnek', file=f)
    print(f'=========================================', file=f)
    for fgh in hgf:
        print(f"Név: {fgh['Név']}, Életkor: {fgh['Életkor']}, Fizetés: {fgh['Fizetés']} Ft", file=f)
    print("\n" + f' Összesen: {a} fő', file=f)