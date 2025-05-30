# models/jegyfoglalas.py

class JegyFoglalas:
    def __init__(self, utas_neve, jarat, datum):
        """
        Egy új jegyfoglalás létrehozása.
        :param utas_neve: str
        :param jarat: Jarat példány
        :param datum: str (pl. '2025-06-01')
        """
        self.utas_neve = utas_neve
        self.jarat = jarat
        self.datum = datum

    def __str__(self):
        """
        Szép szöveges megjelenítés a foglalásról.
        """
        return f"{self.utas_neve} - {self.jarat} - {self.datum}"