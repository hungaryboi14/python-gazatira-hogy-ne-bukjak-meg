list = []
with open("./vizsga2024/formula.txt", "r", encoding="utf-8") as file:
    next(file)
    for adatok in file:
        adat = adatok.strip().split(';')
        ad = {'nev':adat[0], 'szuletesi_datum':adat[1], 'nemzetiseg':adat[2]}
        list.append(ad)

print("a) feladat")
print("A magyar pilóta adatai:")
for adat in list:
    if adat['nemzetiseg'] == "magyar":
        print(f"{adat['nev']} - {adat['szuletesi_datum']} - {adat['nemzetiseg']}")

print("")

print("b) feladat")
print("A brit pilóták adatai:")
with open("./vizsga2024/brit.txt", "w", encoding="utf-8") as brit:
    for adat in list:
        if adat['nemzetiseg'] == "brit":
            print(f"{adat['nev']} - {adat['szuletesi_datum']} - {adat['nemzetiseg']}")
            print(f"{adat['nev']} - {adat['szuletesi_datum']} - {adat['nemzetiseg']}", file=brit)

print("")

print("c) feladat")
bpilota = 0
for adat in list:
    if adat['nemzetiseg'] == "brazil":
        bpilota = bpilota+1

print(f'Összesen {bpilota} brazil pilóta van!')