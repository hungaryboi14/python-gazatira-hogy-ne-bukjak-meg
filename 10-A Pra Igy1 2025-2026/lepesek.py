lepesek = []
a = 0
while a != 1:
    inp = input("Add meg a 9 nap lépésszámát szóközzel elválasztva: ")
    ls = list(float, inp.split(" "))
    lepesek.append(ls)
    for adat in lepesek:
        asd = len(adat)
        if asd == 9 and type(inp) == int or float:
            a = 1
        else:
            if type(inp) == str:
                print(f"Számot adj meg!")
                break
            else:
                print(f"Nem adtál meg elég számot! Próbáld újra!")
                break


atlag = sum(ls) / len(ls)
maxf = max(ls)
ossz = sum(ls)
maxn = ls.index(maxf) + 1


print(f"Összes lépés: {ossz}")
print(f"Átlag: {atlag}")
print(f"Maximum: {maxf} (Nap: {maxn})")