diakok = []
with open('aaaaaaaaaaaa/diakok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        diak = {'név': adatok[0], 'életkor': adatok[1], 'átlag': (adatok[2])}
        diakok.append(diak)

print("Diákok adatai:")
for diak in diakok:
    print(f'{diak['név']} - {diak['életkor']} éves, átlag: {diak['átlag']}')

max_kor = 0
for diak in diakok:
    if int(diak['életkor']) > int(max_kor):
        max_kor = diak['életkor']

legidosebbek = []
for diak in diakok:
    if diak['életkor'] == max_kor:
        legidosebbek.append(diak)

print("Legidősebb(ek):")
for diak in legidosebbek:
    print(f" A legidősebb diák(ok) neve(i) {diak['név']} kora(ik): {diak['életkor']}.")

a = 0
for diak in diakok:
    if float(diak['átlag']) > 4.5:
        a = a+1


print(f" A jeles diákok száma: {a}")