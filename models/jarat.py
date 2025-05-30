# models/jarat.py

from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        """
        Alap Jarat osztály konstruktor.
        :param jaratszam: str
        :param celallomas: str
        :param jegyar: int
        """
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        """
        Absztrakt metódus, amit a leszármazott osztályoknak kell megvalósítaniuk.
        """
        pass

    def __str__(self):
        """
        Stringes reprezentáció a járatról.
        """
        return f"{self.jaratszam} - {self.celallomas} ({self.jegyar} Ft)"