def osszeg(cimke, konyv, napi):
    return cimke[konyv] * napi

lista = []
with open('./gyakorlas3a/kolcsonzesek.txt', 'r', encoding='utf-8') as konyvek:
    for sorok in konyvek:
        s = sorok.strip().split(';')

        adats = {'konyv': s[0], 'cimke': s[1], 'napi': int(s[2])}
        lista.append(adats)

asd = 0
while asd == 0:
    cim = input("könyv címe: ")
    napi_bevitel = input("kölcsönzött napok száma: ")
    
    ar = 0
    for f in lista:
        if f['konyv'] == cim:
            ar = f['napi']
    
    if ar > 0:
        napi_szam = int(napi_bevitel)
        if napi_szam > 0:
            szotar_a_fuggvenynek = {cim: ar}
            fizetendo = osszeg(szotar_a_fuggvenynek, cim, napi_szam)
            print(f"Fizetendő: {fizetendo} Ft")
            asd = 1
        else:
            print("Hiba, a napok száma legyen pozitív!")
    else:
        print("Hiba, nincs ilyen könyv, kezdje elölről!")
