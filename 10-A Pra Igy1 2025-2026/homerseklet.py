inp = input("Add meg a 7 nap hőmérsékletét szóközzel elválasztva: ")
fokok = list(map(float, inp.split(" ")))

atlag = sum(fokok) / len(fokok)
minf = min(fokok)
maxf = max(fokok)

minn = fokok.index(minf) + 1
maxn = fokok.index(maxf) + 1

print(f"Átlag: {atlag}")
print(f"Minimum: {minf} (Nap: {minn})")
print(f"Maximum: {maxf} (Nap: {maxn})")