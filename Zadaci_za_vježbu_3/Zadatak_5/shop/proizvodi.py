class Proizvod:
    def __init__(proizvod, naziv, cijena, dostupna_kolicina):
        proizvod.naziv = naziv
        proizvod.cijena = cijena
        proizvod.dostupna_kolicina = dostupna_kolicina

    def ispis(proizvod):
        print(f"Naziv: {proizvod.naziv}")
        print(f"Cijena: {proizvod.cijena}")
        print(f"Dostupna kolicina: {proizvod.dostupna_kolicina}")

skladiste = []

skladiste.append(Proizvod("Slusalice", 120, 10))
skladiste.append(Proizvod("Podloga za miš", 5, 50))
    
def dodaj_proizvod(proizvod):
    if isinstance(proizvod, Proizvod):
        skladiste.append(proizvod)
    else:
        print("Arugument mora biti instanca klase Proizvodi!")

