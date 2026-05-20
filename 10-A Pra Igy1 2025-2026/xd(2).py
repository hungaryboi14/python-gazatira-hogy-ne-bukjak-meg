
autok = []
with open('hd/autok.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'autotipus': adatok[1], 'eletkor': int(adatok[2])}
        autok.append(auto)

print(f'{autok}')


a = 0
b = 0
for tipus in autok:
    for betu in tipus["autotipus"]:
        if betu == "a" or betu == "e" or betu =="A" or betu == "E":
            if betu == "a" or betu == "A":
                a=a+1
            elif betu == "e" or betu == "E":
                b=b+1
    if a != 0 or b != 0:
        print(f'{tipus["autotipus"]} {a} darab "a" betűt és {b} darab e betűt tartalmaz')
    a = 0
    b = 0