fogyasztas = []
a = 0
while a != 1:
    inp = input("Add meg a 7 nap vízfogyasztását literben szóközzel elválasztva: ")
    try:
        ls = list(map(float, inp.split()))
        if len(ls) != 7:
            print("Nem adtál meg elég számot! Próbáld újra!")
        else:
            fogyasztas.append(ls)
            a = 1
    except ValueError:
        print("Számot adj meg!")

atlag = sum(ls) / len(ls)
maxf = max(ls)
ossz = sum(ls)
maxn = ls.index(maxf) + 1

print(f"Össz fogyasztás: {ossz}")
print(f"Átlag: {atlag}")
print(f"Maximum: {maxf} (Nap: {maxn})")