def autokdef(autok): 
    auto = autok.strip().split(',')
    autoa = {'r': auto[0], 't': auto[1], 'e': auto[2]}
    return autoa

autok_lista = []

with open('./iras/autok.csv', "r", encoding="utf-8") as af:
    for sor in af:
        auto = autokdef(sor)
        autok_lista.append(auto)

with open("./iras/a_betus.txt", "w", encoding="utf-8") as f:
    for auto in autok_lista:
        if "A" in auto['r'].upper():
            f.write(f"{auto['r']},{auto['t']},{auto['e']}\n")

a = 0
e = 0

for i in autok_lista:
    for betu in i['t']:
        if betu == 'a':
            a = a + 1
        if betu == 'e':
            e = e + 1


print(a)
print(e)
    

for auto in autok_lista:
    print(f"Az auto rendszáma {auto['r']}, márkája: {auto['t']}, életkora: {auto['e']}")
