class Film:
    def __init__(self, cim, rendezo, ev, hossz_perc):
        self.cim = cim
        self.rendezo = rendezo
        self.ev = ev
        self.hossz_perc = hossz_perc

    def filmxd(self):
        print(f"A {self.cim} filmet {self.rendezo} rendezte {self.ev}-ben és {self.hossz_perc} perc hosszú.")


filmek_adatok = [
    {
        "cim": "A keresztapa",
        "rendezo": "Francis Ford Coppola",
        "ev": 1972,
        "hossz_perc": 175
     },
    {
        "cim": "Forrest Gump",
        "rendezo": "Robert Zemeckis",
        "ev": 1994,
        "hossz_perc": 142
     },
    {
        "cim": "Eredet",
        "rendezo":
        "Christopher Nolan",
        "ev": 2010,
        "hossz_perc": 148
     }
]

filmek = []

for adat in filmek_adatok:
    film = Film(adat['cim'], adat['rendezo'], adat['ev'], adat['hossz_perc'])
    filmek.append(film)

for film in filmek:
    film.filmxd()
