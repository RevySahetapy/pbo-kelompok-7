#REVY RAVLY SABBATHINO SAHETAPY
#5210411227

#Class Abstrak
from abc import ABC, abstractmethod
class Bentuk(ABC) :
    @abstractmethod
    def luas(self) :
        return self._sisi * self._sisi
#5210411227_REVY
    @abstractmethod
    def keliling(self) :
        return 4 * self._sisi

class Persegi(Bentuk) :
    def __init__(self, sisi) :
        self._sisi = sisi
    def luas(self) :#5210411227_REVY
        return self._sisi * self._sisi
    def keliling(self) :
        return 4 * self._sisi 
#5210411227_REVY
persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())