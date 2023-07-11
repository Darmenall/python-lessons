"""
03/02/2021

    Python: 6-lesson

    Avtor: Darmen Allambergenov

    Tema: Dunder metodlari

"""


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""

    def __init__(self, make, model, color, jil, cena):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.color = color
        self.jil = jil
        self.cena = cena
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def __str__(self): #print(avto1)
        """Obyekt haqinda mag'lumat"""
        return f"Avto: {self.make} {self.model}. {self.cena}$"

    def __repr__(self): # Repozition str menen birge print(avto1)
        """Obyekt haqinda mag'lumat"""
        return f"Avto: {self.make} {self.model}. {self.cena}$"

    def __eq__(self, basqa_avto): #==
        return self.cena == basqa_avto.cena

    def __lt__(self, basqa_avto):# <
        return self.cena < basqa_avto.cena

    def __le__(self, basqa_avto): #<=
        return self.cena <= basqa_avto.cena

    def get_info(self):
        return (
            f"{self.color} {self.make} {self.model}.{self.jil}-yil. Cenasi:{self.cena}$"
        )

avto1 = Avto("gm","Malibu", "Qara",2020,40000)
avto2 = Avto("gm","Lacetti", "Aq",2020,20000)
avto3 = Avto("Tayota","CArolla", "kok",2018,45000)
avto4 = Avto("Mazda","6", "qizil",2015,35000)
avto5 = Avto("Volkswagen","POlO", "qara",2015,30000)
avto6 = Avto("Honda","Accord", "aq",2017,42000)
# x,y = 10,20
# x>y
# x<y
# avto1<avto2
# avto1==avto2
# avto1.cena
# avto2.cena
# avto1>avto2
# avto1>=avto2
# tekst = "dadsad"
# len(tekst)



class AvtoSalon:
    """Avtosalon klassi"""

    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self): #print(salon1)
        return f"{self.name} avtosaloni"

    def __len__(self): #len(salon1)
        return len(self.avtolar)

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, value):# salon1[0]=Avto("gm","damas", "Aq",2020,2000)
        if isinstance(value, Avto):
            self.avtolar[index] = value

    def __call__(self):  # salon1()
        return [avto for avto in self.avtolar]

    def add_avto(self, *manis): # isinstance(avto1,Avto) ,isinstance(avto1,AvtoSalon), isinstance(4,int)
        for avto in manis:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyketin' kiritin")

    def get_list(self):
        return [avto for avto in self.avtolar]
salon1 = AvtoSalon("maxAvto")
salon2 = AvtoSalon("avtolider")
salon1.add_avto(avto1,avto2,avto3)
# sanlar = [1,2,3,4]
# sanlar[2]
# salon1[0]
# salon1[1]
# salon1()
salon2.add_avto(avto4,avto5,avto6)
# salon1()
# salon2()



