def ertek(termek, keszlet):
    return keszlet[termek]["db"] * keszlet[termek]["ar"]

keszlet = {}
with open("keszlet.txt", "r", encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        if not sor:
            continue
        reszek = sor.split(";")
        nev = reszek[0]
        db = int(reszek[1])
        ar = int(reszek[2])
        keszlet[nev] = {"db": db, "ar": ar}

print("Összes készletérték:")
teljes = 0
for termek in keszlet:
    e = ertek(termek, keszlet)
    teljes += e
    print(f"  {termek}: {e} Ft")
print(f"Teljes készletérték: {teljes} Ft")

while True:
    nev = input("Melyik termék értékét kéred? ")
    if nev in keszlet:
        print(f"{nev} készletértéke: {ertek(nev, keszlet)} Ft")
        break
    else:
        print("Ismeretlen termék, próbáld újra!")
