import sys
sys.stdout.reconfigure(encoding='utf-8')

from shop import proizvodi, narudzbe

# Lista proizvoda za dodavanje
proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

# Dodavanje proizvoda u skladiste
for p in proizvodi_za_dodavanje:
    novi = proizvodi.Proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])
    proizvodi.dodaj_proizvod(novi)

# Ispis svih proizvoda u skladistu
for p in proizvodi.skladiste:
    p.ispis()

# Kreiranje narudzbe od svih proizvoda u skladistu
lista_za_narudzbu = [{"naziv": p.naziv, "cijena": p.cijena, "narucena_kolicina": p.dostupna_kolicina} 
                     for p in proizvodi.skladiste]

nova_narudzba = narudzbe.napravi_narudzbu(lista_za_narudzbu)

# Ispis narudzbe
if nova_narudzba:
    nova_narudzba.ispis_narudzbe()