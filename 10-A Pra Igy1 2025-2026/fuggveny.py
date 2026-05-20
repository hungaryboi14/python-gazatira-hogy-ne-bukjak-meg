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

print(f'Páros számok listája: {paros}')
print(f'Páratlan számok listája: {paratlan}')