inp = input("Add meg a 5 nap hőmérsékletét szóközzel elválasztva: ")
napi = list(map(float, inp.split(" ")))

atlag = sum(napi) / len(napi)
maxf = max(napi)
maxn = napi.index(maxf) + 1
ossz = sum(napi)

print(f"Az összes eladott darab: {ossz}")
print(f"Átlag: {atlag}")
print(f"Maximum: {maxf} (Nap: {maxn})")