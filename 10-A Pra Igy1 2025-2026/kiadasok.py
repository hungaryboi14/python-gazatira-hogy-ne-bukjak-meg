a = 0
while a != 1:
    kiadas = []
    c = 0
    try:
        szam = input("Szóközzel elválasztva add meg 14 nap kiadását: ")
        a = szam.strip().split(" ")
        for b in a:
            c = int(b)
            kiadas.append(c)
        a = 1
    except:
        print("Hiba!")
        a = 0


ossz = 0
for szam in kiadas:
    ossz = ossz + szam

atlag = ossz/len(kiadas)

nap = 0
legnap = 0
for szam in kiadas:
    if szam > legnap:
        legnap = szam
        nap = nap + 1
    
print(f'Az összes kiadás: {ossz} Ft')

print(f'A kiadások átlaga: {atlag} Ft')

print(f'A legnagyobb kiadás: {nap}. nap, {legnap} Ft')