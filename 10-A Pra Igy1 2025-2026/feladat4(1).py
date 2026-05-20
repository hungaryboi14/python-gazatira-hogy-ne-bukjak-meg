def autokdef(autok): 
    auto = autok.strip().split(',')
    autoa = {'r': auto[0], 't': auto[1], 'e': auto[2]}
    return autoa

def betu(tipus):
    tipus = tipus.lower()
    return tipus.count('a'), tipus.count('e')


autok_lista = []

with open('./iras/autok.csv', "r", encoding="utf-8") as af:
    for sor in af:
        auto = autokdef(sor)
        autok_lista.append(auto)

with open("./iras/a_betus.txt", "w", encoding="utf-8") as f:
    for auto in autok_lista:
        if "A" in auto['r'].upper():
            f.write(f"{auto['r']},{auto['t']},{auto['e']}\n")

for auto in autok_lista:
    a, e = betu(auto['t'])
    print(f"{auto['t']}: a betűk = {a}, e betűk = {e}")

for auto in autok_lista:
    print(f"Az auto rendszáma {auto['r']}, márkája: {auto['t']}, életkora: {auto['e']}")
