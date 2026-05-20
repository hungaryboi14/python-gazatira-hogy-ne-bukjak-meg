csapadekok = []
a = 0
while a != 7:
    cs = float(input("Add meg a 7 nap csapadékértékét mm-ben: "))
    csapadekok.append(cs)
    a = a+1


atlag = sum(csapadekok) / len(csapadekok)
maxf = max(csapadekok)
maxn = csapadekok.index(maxf) + 1
osszes= sum(csapadekok)

print(f"A hét nap össz csapadéka: ")
print(f"Átlag: {atlag}")
print(f"Maximum: {maxf} (Nap: {maxn})")