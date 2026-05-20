import random
with open('./iras/paros.txt', 'w', encoding='utf-8') as paros, \
        open('./iras/paratlan.txt', 'w', encoding='utf-8') as paratlan:
    sz1 = []
    a = 0
    while a != 10:
        sz2 = random.randint(0,50)
        sz1.append(sz2)
        a = a+1
    for sz2 in sz1:
        if sz2 % 2 == 0 :
            print(sz2, file=paros)
        else:
            print(sz2, file=paratlan)