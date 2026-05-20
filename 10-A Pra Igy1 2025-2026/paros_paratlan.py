def osszeg_szamolas(szam, tipus):
    osszeg = 0

    for sz in range(1, szam + 1):
        if tipus == "paros":
            if sz % 2 == 0:
                osszeg = osszeg + sz

        if tipus == "paratlan":
            if sz % 2 == 1:
                osszeg = osszeg + sz

    return osszeg


szam = int(input("Adj meg egy számot: "))

paros_osszeg = osszeg_szamolas(szam, "paros")
paratlan_osszeg = osszeg_szamolas(szam, "paratlan")

print(f"Páros számok összege:", paros_osszeg)
print(f"Páratlan számok összege:", paratlan_osszeg)
