class Auto:
    def __init__(self, marka, evjarat, uzemanyag):
        self.marka = marka
        self.evjarat = evjarat
        self.uzemanyag = uzemanyag



    def indit(self):
        print(f"A(z) {self.marka} ({self.evjarat}) beindult - {self.uzemanyag}-üzemmel.")


auto1 = Auto("BMW", 2010, "dízel")
auto2 = Auto("Toyota", 2018, "hibrid")