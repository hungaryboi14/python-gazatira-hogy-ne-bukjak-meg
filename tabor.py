class Diak:
    def __init__(self, nev, kor, napok):
        self.nev = nev
        self.kor = kor
        self.napok = napok

    def marad(self):
        return self.napok >= 5


diakok = []
with open("diakok.txt", "r", encoding="utf-8") as f:
    sorok = f.readlines()

for sor in sorok[2:]:
    sor = sor.strip()
    if not sor:
        continue
    reszek = sor.split(";")
    nev = reszek[0]
    kor = int(reszek[1])
    napok = int(reszek[2])
    diakok.append(Diak(nev, kor, napok))

hosszabbak = [d for d in diakok if d.marad()]

print(f"Jelentkezett diákok száma: {len(diakok)}")
print(f"Legalább 5 napot maradók száma: {len(hosszabbak)}")
print("\nLegalább 5 napot maradók:")
for d in hosszabbak:
    print(f"{d.nev};{d.kor}")

with open("hosszabb.txt", "w", encoding="utf-8") as f:
    for d in hosszabbak:
        f.write(f"{d.nev};{d.kor}\n")
