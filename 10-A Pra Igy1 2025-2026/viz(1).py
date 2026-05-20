fogyasztas = []
a = 0
while a != 1:
    inp = input("Add meg a 7 nap vízfogyasztását literben szóközzel elválasztva: ")
    ls = list(map(float, inp.split(" ")))
    fogyasztas.append(ls)
    for adat in fogyasztas:
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


atlag = sum(ls) / len(ls)
maxf = max(ls)
ossz = sum(ls)
maxn = ls.index(maxf) + 1


print(f"Össz fogyasztás: {ossz}")
print(f"Átlag: {atlag}")
print(f"Maximum: {maxf} (Nap: {maxn})")