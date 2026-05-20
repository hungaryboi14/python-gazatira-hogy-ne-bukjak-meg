def fizetendo(nev, db):
    for a in ad:
        if nev == a['alkatrész']:
            return db * a['ár']
ad = []
with open("./python/alkatresz/alkatreszek.txt", "r", encoding="utf-8") as f:
    for so in f:
        s = so.strip().split(";")
        a = {'alkatrész': s[0], 'ár': int(s[1])}
        ad.append(a)


asd = 0
while asd != 1:
    n = input(f'Add meg az alkatrész nevét: ')
    for a in ad:
        if n == a['alkatrész']:
            asd = 1
    if asd != 1:
        print(f'Hibás alkatrész név!')
        print(f'')

bsd = 0
while bsd != 1:
    try:
        db = int(input(f'Alkatrész darabszáma: '))
        if db <= 0:
            print(f'Pozitív számot adj meg!')
            bsd = 0
        else:
            bsd = 1
    except:
        print(f'Hibás darabszám!')


print(f'A fizetendő összeg: {fizetendo(n, db)}')
