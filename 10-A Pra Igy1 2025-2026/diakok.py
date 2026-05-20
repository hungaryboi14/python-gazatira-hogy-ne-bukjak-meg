def eletkor(keresztnev, vezeteknev):
    for diakok in adatok:
        if dv == diakok['vezeteknev'] and dk == diakok['keresztnev']:
            return 2026 - diakok['szuletesi_ev']


adatok = []
with open("./diakok_1/diakok.txt", "r", encoding="utf-8") as fajl:
    for sorok in fajl:
        sor = sorok.strip().split(';')
        diakok = {'keresztnev':sor[0], 'vezeteknev':(sor[1]), 'szuletesi_ev':int((sor[2]))}
        adatok.append(diakok)

c = 0
while c != 1:
    q = 0
    while q != 1:
        dv = input(f'Diák vezetékneve: ')
        for diakok in adatok:
            if dv == diakok['vezeteknev']:
                q = 1
            elif q != 1:
                print("Hiba!")
    w = 0
    while w != 1:
        dk = input(f'Diák keresztneve: ')
        for diakok in adatok:
            if dk == diakok['keresztnev']:
                w = 1
            elif w != 1:
                print("Hiba!")

    kor = eletkor(dv, dk)
    if kor == None:
        print(f'Rossz neveket írtál be!')
    else:
        c = 1


print(f'A diák életkora: {kor}')