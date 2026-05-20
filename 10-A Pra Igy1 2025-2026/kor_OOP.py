import random

class Kor:
    def __init__(self, sugar, kozeppont=(0, 0)):
        self.sugar = sugar
        self.kozeppont = kozeppont

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 3.14 * 2

korok = []

kor01 = Kor(5, (3, 7))
print(kor01.kozeppont)
print(kor01.terulet())
print(kor01.kerulet())

kor02 = Kor(10, (1, 1))
print(kor02.kozeppont)
print(kor02.terulet())
print(kor02.kerulet())

kor03 = Kor(5)
print(kor03.terulet())
print(kor03.kerulet())
print(kor03.kozeppont)


for _ in range(5):
    kor = Kor(random.randint(1, 10))
    korok.append(kor)

for kor in korok:
    print(kor.sugar, kor.kerulet())