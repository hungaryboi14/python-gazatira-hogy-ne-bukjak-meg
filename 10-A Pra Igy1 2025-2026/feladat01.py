a = input("Kérem adja meg egy iskola nevét (pl.: Petrik Lajos Technikum): ")

b = int(input("Kérem adja meg hány tanulója volt az iskolának az elmúlt tanévben: "))

c = int(input("Kérem adja meg hány tanuló nem fizette be az alapítványi hozzájárulást az elmúlt tanévben: "))

d = 5000 * (b - c)

print(f'A(z) {a} alapítványának a bevétele az előző tanévben: {d} Ft')

if d > 3000000:
    print(f'A(z) {a} alapítványának a működése sikeres volt.')
else:
    print(f'A(z) {a} alapítványának a működése sikertelen volt.')



