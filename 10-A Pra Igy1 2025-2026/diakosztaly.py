class Diak:
    def __init__(self, nev, eletkor, osztaly):
        self.nev = nev
        self.eletkor = eletkor
        self.osztaly = osztaly

    def bemutatkozik(self):
        print(f"Szia, {self.nev} vagyok, {self.eletkor} éves, a {self.osztaly} osztályba járok.")

d1 = Diak("Anna", 18, "13.A")
d2 = Diak("Bence", 19, "13.A")