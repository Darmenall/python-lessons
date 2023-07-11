"""

    Python: 14-lesson

    Avtor: Darmen Allambergenov

    Tema: INKAPSULIYATCIYA HA'M KLASSGA TIYSLI QALIYETLER HA'M METODLAR

"""
# from uuid import uuid4
# class Avto:
#     def __init__(self, make, model, color, age, summa, km=0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.age = age
#         self.summa = summa
#         self.__km = km
#         self.__id = uuid4()

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self, km):
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashinin' km qaytarip bolmaydi")

# avto1 = Avto("GM", 'Malibu', 'Qara', 2023, 40000, 0)
# print(f'ID: {avto1.get_id()}')
# avto1.add_km(1500)
# print(avto1.get_km())


# =============================================================================
#               klasslardim ozgeshe (ozine tiysli qasiyetleri)
# =============================================================================

# from uuid import uuid4
# class Avto:
#     __num_avto = 0
#     def __init__(self, make, model, color, age, summa, km=0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.age = age
#         self.summa = summa
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self, km):
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashinin' km qaytarip bolmaydi")


# avto1 = Avto("GM", 'Malibu', 'Qara', 2023, 40000, 0)
# avto2 = Avto("GM", 'Lacetti', 'Aq', 2015, 20000, 50000)
# avto3 = Avto("Tayota", 'Carolla', 'kok', 2019, 50000, 32000)
# print(Avto.get_num_avto())


# =============================================================================
#                              DUNDER METODLARI
#                              double and scor
# =============================================================================

# from uuid import uuid4
# class Avto:
#     __num_avto = 0
#     def __init__(self, make, model, color, age, summa, km=0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.age = age
#         self.summa = summa
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#
#     def __str__(self):
#         return f"Avto: {self.make} {self.model}"
#
#     def __repr__(self):  # REPREZENTION
#         return f"Avto: {self.make} {self.model}"
#
# # =============================================================================
# #                      salistiriw metodlari
# # =============================================================================
#
#     def __eq__(self, y):
#         return self.summa == y.summa
#
#     def __lt__(self, y):
#         return self.summa < y.summa
#
#     def __le__(self, y):
#         return self.summa <= y.summa
#
#
# avto1 = Avto("GM", 'Malibu', 'Qara', 2023, 40000, 0)
# print(avto1)
#
# avto2 = Avto("GM", 'Lacetti', 'Aq', 2015, 20000, 50000)
#
# # x,y = 10,20
# # x>y
# # y>x
#
# class Avtosalon:
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#
#     def __getitem__(self, index):
#         return self.avtolar[index]
#
#     # salon1[0] = Avto("BMW", 'x7', "qara", 2020, 70000)
#     def __setitem__(self, index, manis):
#         self.avtolar[index] = manis
#
#     def add_avto(self, *manis):
#         # isinistance(4, int)
#         # isinistance("dasd", str)
#         # isinistance(avto1, Avto)
#         for avto in manis:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("avto jazin'")
#
#     # def __call__(self):
#     #     return [avto for avto in self.avtolar]
#
#     def __call__(self, *manis):
#         if manis:
#             for avto in manis:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]
#
#
#
# salon1 = Avtosalon("MaxAvto")
#
# avto1 = Avto("GM", 'Malibu', 'Qara', 2023, 40000, 0)
# avto2 = Avto("GM", 'Lacetti', 'Aq', 2015, 20000, 50000)
# avto3 = Avto("Tayota", 'Carolla', 'kok', 2019, 50000, 32000)
# salon1.add_avto(avto1, avto2, avto3)
#
# # salon1[0] no
#
# # salon1[0]
# # Out[24]: Avto: GM Malibu
#
# # salon1[1]
# # Out[25]: Avto: GM Lacetti
#
# # salon1[:]
# # Out[26]: [Avto: GM Malibu, Avto: GM Lacetti, Avto: Tayota Carolla]
#
# avto4 = Avto("GM", 'matiz', 'aq', 2016, 10000, 35400)
# avto5 = Avto("GM", 'damas', 'Aq', 2015, 12000, 34000)
# avto6 = Avto("Tayota", 'Camri', 'kok', 2019, 50000, 32000)
