from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraza: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")

# Kreiranje objekta
auto1 = Automobil("Volkswagen", "Golf MK4", 2001, 220000)

# Pozivanje metoda
auto1.ispis()
auto1.starost()
