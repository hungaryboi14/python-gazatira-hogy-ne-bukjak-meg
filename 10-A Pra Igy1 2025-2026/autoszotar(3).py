autok = [
{'marka': 'Audi', 'kobcenti': 2500},
{'marka': 'BMW', 'kobcenti': 3000},
{'marka': 'Opel', 'kobcenti': 1600},
{'marka': 'Mercedes', 'kobcenti': 2200},
{'marka': 'Volkswagen', 'kobcenti': 2000},
{'marka': 'Toyota', 'kobcenti': 1800},
{'marka': 'Honda', 'kobcenti': 1700},
{'marka': 'Ford', 'kobcenti': 1600},
{'marka': 'Kia', 'kobcenti': 1400},
{'marka': 'Hyundai', 'kobcenti': 1500},
{'marka': 'Mazda', 'kobcenti': 1900},
{'marka': 'Subaru', 'kobcenti': 2000},
{'marka': 'Peugeot', 'kobcenti': 1600},
{'marka': 'Renault', 'kobcenti': 1300},
{'marka': 'Fiat', 'kobcenti': 1200}
]

l = []

for auto in autok:
    if auto['kobcenti'] > 2000:
        l.append(auto)


for auto in l:
    print(f"A {auto['marka']} márkájú autó {auto['kobcenti']} köbcentis.")