import random

def f(szamok):
    for szam in szamok:
        if szam % 2 == 0:
            paros.append(szam)
        else:
            paratlan.append(szam)

paros = []
paratlan = []
szamok = []
a = 0
while a != 30:
    szam = random.randint(1,100)
    szamok.append(szam)
    a = a+1


f(szamok)
with open('./paros.txt', 'w', encoding='utf-8') as parosf:
    print(f'Páros számok listája: {paros}', file=parosf)

with open('./paratlan.txt', 'w', encoding='utf-8') as paratlanf:
    print(f'Páratlan számok listája: {paratlan}', file=paratlanf)