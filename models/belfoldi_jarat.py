# models/belfoldi_jarat.py

from models.jarat import Jarat

class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"

    def __str__(self):
        return f"[Belföldi] {super().__str__()}"