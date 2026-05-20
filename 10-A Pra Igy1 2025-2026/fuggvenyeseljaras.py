a = int(input("add meg az első számot! "))
b = int(input('Add meg a második számot: '))

def osszead(x, y):
    eredmeny = x + y
    print('A két szám összege: ', eredmeny)

def szamolo(x, y):
    return a - b

print(f' A számaid különbsége: {szamolo(a, b)}')
osszead(a, b)
