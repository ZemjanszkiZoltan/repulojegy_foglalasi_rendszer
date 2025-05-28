# utils/adatkezelo.py

import json
import os
from models.belfoldi_jarat import BelfoldiJarat
from models.nemzetkozi_jarat import NemzetkoziJarat
from models.legitarsasag import LegiTarsasag
from models.jegyfoglalas import JegyFoglalas

def inicializal_rendszer():
    """
    Létrehozza a légitársaságot, járatokat és betölti a foglalásokat.
    """
    legitarsasag = LegiTarsasag("SkyLine Airlines")

    # Létrehozunk 3 járatot
    jarat1 = BelfoldiJarat("B001", "Budapest", 15000)
    jarat2 = BelfoldiJarat("B002", "Debrecen", 10000)
    jarat3 = NemzetkoziJarat("N001", "London", 80000)

    legitarsasag.jarat_hozzaadasa(jarat1)
    legitarsasag.jarat_hozzaadasa(jarat2)
    legitarsasag.jarat_hozzaadasa(jarat3)

    # Csak töltsük be a foglalásokat a JSON-ból
    foglalasok = foglalasok_betoltese(legitarsasag)

    # Nem kell alapfoglalásokat generálni, mert már van a JSON fájlban

    return legitarsasag, foglalasok

def foglalasok_mentese(foglalasok, fajlnev="foglalasok.json"):
    """
    Elmenti a foglalásokat JSON fájlba.
    """
    adat = []
    for f in foglalasok:
        adat.append({
            "utas_neve": f.utas_neve,
            "jaratszam": f.jarat.jaratszam,
            "datum": f.datum
        })
    with open(fajlnev, "w", encoding="utf-8") as f:
        json.dump(adat, f, ensure_ascii=False, indent=4)


def foglalasok_betoltese(legitarsasag, fajlnev="foglalasok.json"):
    """
    Betölti a foglalásokat a JSON fájlból, és visszaadja a JegyFoglalas listát.
    """
    from models.jegyfoglalas import JegyFoglalas

    if not os.path.exists(fajlnev):
        return []

    with open(fajlnev, "r", encoding="utf-8") as f:
        adat = json.load(f)

    foglalasok = []
    for elem in adat:
        jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == elem["jaratszam"]), None)
        if jarat:
            foglalasok.append(JegyFoglalas(elem["utas_neve"], jarat, elem["datum"]))
    return foglalasok