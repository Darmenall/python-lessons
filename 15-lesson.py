"""

    Python: 14-lesson

    Avtor: Darmen Allambergenov

    Tema: INKAPSULIYATCIYA HA'M KLASSGA TIYSLI QALIYETLER HA'M METODLAR

"""

from uuid import uuid4


class Avto:
    """Avtomobil klassi"""

    def __init__(self, make, model, color, jil, cena, km=0):
        """avtomobildin' qasiyeti """
        self.make = make
        self.model = model
        self.rang = color
        self.yil = jil
        self.narh = cena
        self.__km = km
        self.__id = uuid4()

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinin' km ge taza km qosiw"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashinin' km qaytarip  bolmaydi")

"""
print(uuid4())
print(uuid4())
print(uuid4())
print(uuid4())
avto1 = Avto("GM", "Malibu", "Qara", 2020, 40000, 1000)
avto1.cane
avto1.model
avto.__km
avto1.get_km()
avto1.get_id()
avto1.get_km(2000)
avto1.get_km()
avto1.get_km(-2000)

"""


avto1 = Avto("GM", "Malibu", "Qara", 2020, 40000, 1000)
# print(f"ID: {avto1.get_id()}")
# avto1.add_km(1500)
# print(avto1.get_km())




from uuid import uuid4


class Avto:
    """Avtomobil klassi"""
    __num_avto = 0  # __ inkapsuliyatciya , num_avto-classgatiysli
    def __init__(self, make, model, color, jil, cena, km=0):
        """avtomobildin' qasiyeti """
        self.make = make
        self.model = model
        self.rang = color
        self.yil = jil
        self.narh = cena
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    @classmethod  # DEKORATOR
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

avto1 = Avto("GM", "Malibu", "Qara", 2020, 40000, 1000)
avto2 = Avto("GM", "lacetti", "Aq", 2020, 20000, 1000)
avto3 = Avto("Tayota", "Carolla", "ko'k", 2020, 40000, 1000)

"""
avto1
avto2
avto3
avto1.num_avto
avto2.num_avto
++++
__
Avto.get_num_avto()
avto1 = Avto("GM", "Malibu", "Qara", 2020, 40000, 1000)
avto2 = Avto("GM", "lacetti", "Aq", 2020, 20000, 1000)
avto3 = Avto("Tayota", "Carolla", "ko'k", 2020, 40000, 1000)
Avto.get_num_avto()
avto1.get_num_avto()

modul
from avto import Avto 

"""





class Bus:
    pass


class Train:
    pass
