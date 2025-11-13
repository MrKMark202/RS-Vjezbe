narudzbe = []

class Narudzba:
    def __init__(narudzba, naruceni_proizvodi, ukupna_cijena):
        narudzba.naruceni_proizvodi = naruceni_proizvodi
        narudzba.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_str = ", ".join(
            f"{p['naziv']} x {p['narucena_kolicina']}" 
            for p in self.naruceni_proizvodi
        )
        print(f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        print("Atgument mora biti lista!")
        return None
    if len(lista_proizvoda) ==0:
        print("Lista ne smije biti prazna!")
        return None
    for p in lista_proizvoda:
        if not isinstance(p, dict):
            print("Svaki proizvod mora biti rječnik!")
            return None
        if not all(k in p for k in ["naziv", "cijena", "narucena_kolicina"]):
            print("Svaki proizvod mora sadržavati ključeve: naziv, cijena, narucena_kolicina!")
            return None
        if p["narucena_kolicina"] > p.get("dostupna_kolicina", p["narucena_kolicina"]):
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None


    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in lista_proizvoda)


    nova_narudzba = Narudzba(lista_proizvoda, ukupna_cijena)
    narudzbe.append(nova_narudzba)
    return nova_narudzba