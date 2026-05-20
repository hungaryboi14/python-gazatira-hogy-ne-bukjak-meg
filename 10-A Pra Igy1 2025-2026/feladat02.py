import random


def Generalas(honapokSzama):
    for i in range(honapokSzama):
        a = random.randint(20,30)
        havi.append(str(a))


def osztalypenz():
    gyult = 0
    for ha in havi:
        gyult = gyult + (int(ha) * 1000)
    return gyult

havi = []

a = input("Végzős az osztályod? (igen/nem) ")
if a == 'igen':
    honapokSzama = 8
if a == 'nem':
    honapokSzama = 10



Generalas(honapokSzama)



print(f'A befizetések száma havonta: {(', ').join(havi)}')
print(f'Osztálypénz: {osztalypenz()} Ft.')