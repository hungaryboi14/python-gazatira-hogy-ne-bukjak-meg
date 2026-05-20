def main():
    a = []

    while True:
        c = int(input("Adj meg egy számot: "))

        if c < 0:
            break
        a.append(c)

    if a:
        legkisebb = b(a)
        print(f"A megadott legkisebb szám: {legkisebb}")

def b(szamok):
    return min(szamok)



main()
