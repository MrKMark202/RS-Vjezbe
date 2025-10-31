def validiraj_broj_telefona(broj: str):
    # Tablice pozivnih brojeva
    fiksne = {
        "01": "Grad Zagreb i Zagrebačka županija",
        "020": "Dubrovačko-neretvanska županija",
        "021": "Splitsko-dalmatinska županija",
        "022": "Šibensko-kninska županija",
        "023": "Zadarska županija",
        "031": "Osječko-baranjska županija",
        "032": "Vukovarsko-srijemska županija",
        "033": "Virovitičko-podravska županija",
        "034": "Požeško-slavonska županija",
        "035": "Brodsko-posavska županija",
        "040": "Međimurska županija",
        "042": "Varaždinska županija",
        "043": "Bjelovarsko-bilogorska županija",
        "044": "Sisačko-moslavačka županija",
        "047": "Karlovačka županija",
        "048": "Koprivničko-križevačka županija",
        "051": "Primorsko-goranska županija",
        "052": "Istarska županija",
        "053": "Ličko-senjska županija"
    }

    mobilne = {
        "091": "A1 Hrvatska",
        "092": "Tomato",
        "095": "Telemach",
        "097": "bonbon",
        "098": "Hrvatski telekom",
        "099": "Hrvatski telekom"
    }

    posebne = {
        "0800": "Besplatni pozivi",
        "060": "Komercijalni pozivi",
        "061": "Glasovanje telefonom",
        "064": "Usluge s neprimjerenim sadržajem",
        "065": "Nagradne igre",
        "069": "Usluge namijenjene djeci",
        "072": "Jedinstveni pristupni broj za cijelu državu"
    }

    # Čišćenje broja
    for znak in [" ", "-", "(", ")", "\t"]:
        broj = broj.replace(znak, "")
    if broj.startswith("+"):
        broj = broj[1:]
    if broj.startswith("00385"):
        broj = broj[5:]
    elif broj.startswith("385"):
        broj = broj[3:]

    # Provjera da su ostali znakovi znamenke
    if not broj.isdigit():
        return {"validan": False}

    rezultat = {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    # Pronalaženje pozivnog broja
    pozivni = None
    if broj[:4] in posebne:
        pozivni = broj[:4]
    elif broj[:3] in mobilne:
        pozivni = broj[:3]
    elif broj[:3] in fiksne:
        pozivni = broj[:3]
    elif broj[:2] in fiksne:
        pozivni = broj[:2]

    if not pozivni:
        return rezultat

    ostatak = broj[len(pozivni):]

    rezultat["pozivni_broj"] = pozivni
    rezultat["broj_ostatak"] = ostatak

    # Provjera i određivanje vrste
    if pozivni in fiksne:
        rezultat["vrsta"] = "fiksna mreža"
        rezultat["mjesto"] = fiksne[pozivni]
        rezultat["operater"] = None
        if 6 <= len(ostatak) <= 7:
            rezultat["validan"] = True
    elif pozivni in mobilne:
        rezultat["vrsta"] = "mobilna mreža"
        rezultat["mjesto"] = None
        rezultat["operater"] = mobilne[pozivni]
        if 6 <= len(ostatak) <= 7:
            rezultat["validan"] = True
    elif pozivni in posebne:
        rezultat["vrsta"] = "posebne usluge"
        rezultat["mjesto"] = None
        rezultat["operater"] = None
        if len(ostatak) == 6:
            rezultat["validan"] = True

    return rezultat


# --- PRIMJERI ---
print(validiraj_broj_telefona("+385 91 721 7633"))
print(validiraj_broj_telefona("021 334 556"))
print(validiraj_broj_telefona("00385-0800-123456"))
print(validiraj_broj_telefona("(385)0993332222"))
