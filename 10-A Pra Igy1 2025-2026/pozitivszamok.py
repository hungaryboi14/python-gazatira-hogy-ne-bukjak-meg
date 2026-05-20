a = 1
szam = []
while a > 0:
    a = (int(input("Adj meg egy számot: ")))
    if a >= 0:
        szam.append(a)

def szamolo():
    return(min(szam))

print(f' A legkisebb számod: {szamolo()}')