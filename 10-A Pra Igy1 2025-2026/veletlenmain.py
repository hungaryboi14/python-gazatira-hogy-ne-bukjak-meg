import random


def bekeres():
    a = int(input("Adj meg egy számot: "))
    return a

def main():
    szam = random.randint(1, 10)
    print("A kezdő szám:", szam)

    while True:
        bevitel = bekeres()

        if bevitel == 0:
            break

        szam = bevitel
        print("A szám új értéke:", szam)

main()
