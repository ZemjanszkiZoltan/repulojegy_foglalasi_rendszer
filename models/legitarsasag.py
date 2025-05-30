# models/legitarsasag.py

class LegiTarsasag:
    def __init__(self, nev):
        """
        Létrehozza a légitársaságot egy adott névvel és egy üres járatlistával.
        :param nev: str
        """
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        """
        Hozzáad egy járatot a légitársasághoz.
        :param jarat: Jarat példány
        """
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        """
        Kilistázza a légitársaság összes járatát.
        """
        for jarat in self.jaratok:
            print(jarat)