class Versenyzo:
    def __init__(self, nev, rajtszam, ido):
        self.nev = nev
        self.rajtszam = rajtszam
        self.ido = ido

    def jo(self):
        return self.ido <= 3600

ver = []

with open('./gyakorlas2/versenyzok.txt', 'r', encoding='utf-8') as f:
    next(f)
    next(f)
    for sor in f:
        s = sor.strip().split(';')
        v = Versenyzo(s[0], s[1], int(s[2]))
        ver.append(v)

jo = 0

with open('./gyakorlas2/sikeres.txt', 'w', encoding='utf-8') as f_ki:
    for v in ver:
        if v.jo():
            jo = jo + 1
            print(v.nev)
            print(v.nev, file=f_ki)

print(f"Összes induló: {len(ver)}")
print(f"1 órán belül futottak: {jo}")