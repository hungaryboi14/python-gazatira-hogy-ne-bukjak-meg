def osszeg(arak, film, db):
    return arak[film] * db

filmek_listaja = []
with open('./gyakorlas2/jegyek.txt', 'r', encoding='utf-8') as progik:
    for sorok in progik:
        s = sorok.strip().split(';')
        adats = {'film': s[0], 'arak': int(s[1])}
        filmek_listaja.append(adats)

asd = 0
while asd == 0:
    film_nev = input("Film címe: ")
    db_szoveg = input("Darabszám: ")

    ar = 0
    for f in filmek_listaja:
        if f['film'] == film_nev:
            ar = f['arak']

    if ar > 0:
        db = int(db_szoveg)
        if db > 0:
            szotar_a_fuggvenynek = {film_nev: ar}
            fizetendo = osszeg(szotar_a_fuggvenynek, film_nev, db)
            print(f"Fizetendő: {fizetendo} Ft")
            asd = 1
        else:
            print("Hiba, kezdje elölről!")