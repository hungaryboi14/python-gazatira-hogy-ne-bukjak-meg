autok = []
asd = []
with open('py/auto/autok.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        auto = {'marka': adatok[0], 'autotipus': adatok[1], 'gyartasiev': int(adatok[2]), 'szin': (adatok[3]), 'rendszam': (adatok[4]), 'kobcenti': int(adatok[5]), 'loero': (adatok[6])}
        autok.append(auto)

for auto in autok:
    print(f'Az autó márkája: {auto["marka"]}, típusa: {auto["autotipus"]}, életkora: {auto["gyartasiev"]}, színe: {auto["szin"]}, rendszáma: {auto["rendszam"]}, köbcentije: {auto["kobcenti"]}, lóereje: {auto["loero"]}')

print()
l = []

for auto in autok:
    if auto['kobcenti'] >2500:
           l.append(auto)


for auto in l:
    print(f'Az autó márkája: {auto["marka"]}, típusa: {auto["autotipus"]}, életkora: {auto["gyartasiev"]}, színe: {auto["szin"]}, rendszáma: {auto["rendszam"]}, köbcentije: {auto["kobcenti"]}, lóereje: {auto["loero"]}')

