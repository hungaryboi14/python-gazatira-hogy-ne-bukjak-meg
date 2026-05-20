class Kavefozo:
    def __init__(self, marka, teljesitmeny, tartaly):
        self.marka = marka
        self.teljesitmeny = teljesitmeny
        self.tartaly = tartaly

    def fozi(self):
        print(f" A {self.marka} kávéfőző {self.teljesitmeny}W teljesítménnyel lefőzött egy {self.tartaly} ml-es kávét.")


fozo1 = Kavefozo("Philips", 1200, 250)
fozo2 = Kavefozo("DeLonghi", 1500, 300)

fozo1.fozi()
fozo2.fozi()