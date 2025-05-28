# main.py

from utils.adatkezelo import inicializal_rendszer
from models.jegyfoglalas import JegyFoglalas
from datetime import datetime

def datum_ervenyes(datum_str):
    try:
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        return datum >= datetime.today()
    except ValueError:
        return False


def main():
    legitarsasag, foglalasok = inicializal_rendszer()

    while True:
        print("\n=== Repülőjegy Foglalási Rendszer ===")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("0. Kilépés")

        valasztas = input("Választás: ")

        if valasztas == "1":
            utas_nev = input("Utas neve: ")
            legitarsasag.jaratok_listazasa()
            jaratszam = input("Járatszám: ")
            datum = input("Utazás dátuma (ÉÉÉÉ-HH-NN): ")
            if not datum_ervenyes(datum):
                print("Hiba: Érvénytelen vagy múltbeli dátum.")
                continue


            # Keresd meg a járatot a légitársaság járatai között
            jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == jaratszam), None)
            if jarat:
                uj_foglalas = JegyFoglalas(utas_nev, jarat, datum)
                foglalasok.append(uj_foglalas)
                print(f"Sikeres foglalás! Ár: {jarat.jegyar} Ft")
            else:
                print("Hiba: A megadott járatszám nem létezik.")

        elif valasztas == "2":
            utas_nev = input("Add meg a lemondandó foglalás utas nevét: ")
            jaratszam = input("Add meg a lemondandó foglalás járatszámát: ")

            # Megkeressük a foglalást
            foglalas = next((f for f in foglalasok if f.utas_neve == utas_nev and f.jarat.jaratszam == jaratszam), None)
            if foglalas:
                foglalasok.remove(foglalas)
                print("Foglalás sikeresen törölve!")
            else:
                print("Hiba: A megadott foglalás nem található.")

        elif valasztas == "3":
            print("\n=== Foglalások ===")
            for f in foglalasok:
                print(f)
            if not foglalasok:
                print("Nincs aktív foglalás.")

        elif valasztas == "4":
            print("\n=== Elérhető járatok ===")
            legitarsasag.jaratok_listazasa()

        elif valasztas == "0":
            print("Kilépés a programból. Viszlát!")
            break

        else:
            print("Érvénytelen választás, próbáld újra!")

if __name__ == "__main__":
    main()