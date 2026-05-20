while True:
    try:
        bevitel = input("Adj meg 9 nap lépésszámát szóközzel elválasztva: ")
        reszek = bevitel.split()
        if len(reszek) != 9:
            print(f"Hiba: {len(reszek)} értéket adtál meg, pontosan 9 kell!")
            continue
        lepesek = [int(x) for x in reszek]
        break
    except ValueError:
        print("Hiba: minden érték egész szám kell legyen!")

osszes = sum(lepesek)
atlag = osszes / 9
maximum = max(lepesek)
legjobb_nap = lepesek.index(maximum) + 1

print(f"Összes lépés: {osszes}")
print(f"Átlag: {atlag:.2f}")
print(f"Legaktívabb nap: {legjobb_nap}. nap ({maximum} lépés)")
