# models/nemzetkozi_jarat.py

from models.jarat import Jarat

class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"

    def __str__(self):
        return f"[Nemzetközi] {super().__str__()}"