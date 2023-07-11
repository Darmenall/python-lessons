"""

    Python 4-lesson

    Avtor: Darmen Allambergenov

    Tema: List

"""

# radius = 10
# ati = "Maxset"
#
# miyweler = ['alma', 'anjir', 'erik', 'mandarin']  # miyweler dizimi
# cenalar = [6000, 18000, 10500, 22000]  # cenalar dizimi
# sanlar = ["bir", "eki", 3, 4, 5]  # sanlar mn Harbler aralas dizim
# atlar = []  # Bos dizim
#
# print("Birinshi miywe: ", miyweler[0])
# print("Birinshi miywe: ", miyweler[1])
#
# print("Birinshi miywe: ", miyweler[0].title())
# print("Birinshi miywe: ", miyweler[1].upper())
#
# cenalar = [6000, 18000, 10500, 22000]
# print(cenalar[0]+cenalar[3])
#
# car_models = ['Tayota', 'Gm', 'Volvo', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# print(car_models[-1])  # listin' eng' aqirg'i elementi
#
# # Elemetlerdi ozgertiw
#
# cenalar = [6000, 18000, 10500, 22000]
# cenalar[0] = 7000
# cenalar[2] = 1300
# cenalar[3] = 17000
# print(cenalar)
#
# # .append dizimge qosiw
#
# miyweler = ['alma', 'anjir', 'erik', 'mandarin']
# miyweler.append("juzim")
# print(miyweler)
#
# cars = []
# cars.append("Lasetti")
# cars.append("Nexia 3")
# cars.append("Cobalt")
# print(cars)
#
# # .insert    belgili bir jerge qosiw
#
# cars = ['Lasetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu')
# print(cars)
# cars.insert(2, 'Damas')
# print(cars)
#
# # del indexqa qarab udalit etiw
#
# cars = []
# cars.append("Malibu")
# cars.append("Nexia 3")
# cars.append("Cobalt")
# del cars[1]
# print(cars)
# cars.insert(0, 'Gentra')
# print(cars)

# # .remove  udalit etiw
#
# cars = ['Lasetti', 'Nexia 3', 'Cobalt']
# cars.remove("Nexia 3")
# print(cars)
#
# qaywanlar = ['it', 'pishiq', 'siyr', 'qoy', 'qoyan', 'pishiq']
# qaywanlar.remove("pishiq")
# print(qaywanlar)


# # .pop aliw
#
# bazarliq = ['may', 'un', 'pyaz', 'banan', "go'sh"]
# alingan_zatlar = bazarliq.pop(3)
# alingan_zatlar = bazarliq.pop()
# # print(bazarliq)
# # print(alingan_zatlar)
# print("men " + alingan_zatlar + " satib aldim")
# print("Alinbagan zatlar", bazarliq)

# # .sort()
#
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# cars.sort()
# print(cars)
#
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# cars.sort(reverse=True)
# print(cars)

# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# print(sorted(cars))
# print(sorted(cars, reverse=True))
#
# # sanlli list
#
# ages = [12, 32, 53, -22, 46, 34, 35, 24, -3, -32]
# ages.sort()
# print(ages)
#
# # aqirinan baslap shigaratin
#
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# cars.reverse()
# print(cars)
#
# #   len     listtin' uzinlig'i
#
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# print(len(cars))
# print(f"Sizde {len(cars)} elementen ibarat dizim bar")


# # RANGE()
#
# sanlar = list(range(0, 11))
# print(sanlar)
# sanlar_jup = list(range(2, 11, 2))
# print(sanlar_jup)
# sanlar_taq = list(range(1, 11, 2))
# print(sanlar_taq)
#
# # MIN() MAX() SUM()
#
# cenalar = [6000, 18000, 10500, 22000]
# arzan = min(cenalar)
# print(arzan)
# qimbat = max(cenalar)
# print(qimbat)
# obshi = sum(cenalar)
# print(obshi)

# # dizimdi kesiw
#
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# # my_cars = cars[0:3]
# my_cars = cars[2:5]
# print(cars[:3])
# print(cars[4:])
# print(cars[:])
# print(cars[::2])
# print(my_cars)

# dizimnen kopya aliw
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# my_cars = cars
# # print(cars)
# # print(my_cars)
# my_cars.remove("Volvo")
# print(my_cars)
# my_cars[0] = 'Lacceti'
# print(my_cars)
# print(cars)
# cars.append('Damas')
# print(my_cars)
#
# cars = ['Tayota', 'Gm', 'Volvo', 'Audi', 'BMW', 'Kia', 'Hyundai', 'Volkswagen']
# my_cars = cars[:]
# my_cars.remove('Gm')
# print(cars)
# print(my_cars)

# # TUPLE
#
# texnika = ('avtomobil', 'samaliot', 'vertaliot', 'tank')
# print(texnika[0:3])
# # texnika[0] = 'keme'
# # texnika.append('keme')
# # texnika.remove('avtomobil')
# texnika = list(texnika)
# print(type(texnika))
# texnika.append('keme')
# print(texnika)
# texnika = tuple(texnika)
# print(type(texnika))

