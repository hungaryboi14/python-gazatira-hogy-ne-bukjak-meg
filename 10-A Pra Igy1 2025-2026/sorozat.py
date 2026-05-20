lepesek = []
a = 0
while a != 1:
    inp = input("Add meg a 7 epizód hosszát percben szóközzel elválasztva: ")
    ls = list(map(float, inp.split(" ")))
    lepesek.append(ls)
    for adat in lepesek:
        asd = len(adat)
        if asd == 7 and type(inp) == int or float:
            a = 1
        else:
            if type(inp) == str:
                print(f"Számot adj meg!")
                break
            else:
                print(f"Nem adtál meg elég számot! Próbáld újra!")
                break



maxf = max(ls)
maxn = ls.index(maxf) + 1
ossz = sum(ls)
osszora = sum(ls) / 60

print(f"A 7 epizód hossza percben: {ossz}")
print(f"A 7 epizód hossza órában: {osszora}")
print(f"leghosszabb epizód: {maxf} (sorszám: {maxn})")