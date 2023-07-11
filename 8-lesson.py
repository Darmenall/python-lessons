"""

    Python: 6-lesson

    Avtor: Darmen Allambergenov

    Tema: (Dictionary)

    Sózlik(key): Túsindirme
    giltsoz - manis

"""
# car_0 = {'model': 'ferrari', 'color': 'qara'}
# print(car_0['model'])
# print(car_0['color'])
#
# en_qq = {'apple': 'alma', 'apricot': 'erik', 'banana': 'banan'}

# miyweler = {'alma': "6000", 'erik': '15000', 'banan': '22000'}
# print(f"Almanin' cenasi {miyweler['alma']} so'm")
# print(miyweler['banana'])

# miywe = input('Qanday miywe kerek?: ')
# miyweler = {'alma': "6000", 'erik': '15000', 'banan': '22000'}
# print(f"{miywe} - {miyweler[miywe]} so'm")

# # Sózlik qalegen mag turin' saqlawi mumkin
# student_0 = {'ati': "Maxsetbaev Timur", 'jasi': 20, 't_jili': 2003}
# print(f"{student_0['ati'].title()}, "
#       f"{student_0['t_jili']}-jilda tuwilgan, "
#       f"{student_0['jasi']} jasta")
#
# # taza Sózlik(key) ha'm Túsindirme qosiw mumkin
# student_0['kurs'] = 4
# student_0['fakultet'] = 'Telekom'
# # student_0['ati'] = 'Murat'

# # Bos Sózlik jaratiw
# student_1 = {}
# student_1['ati'] = 'Djoldasbaev Bayram'
# student_1['kurs'] = 3
# student_1['jasi'] = 24
# print(student_1)
# print(f"student {student_1['ati'].title()} {student_1['kurs']}-kursta oqiydi")
#
# # Túsindirme jag'alaw
# student_1['kurs'] = 4
# print(f"student {student_1['ati'].title()} {student_1['kurs']}-kursta oqiydi")

# # Sózlikten elementti oshiriw
# student_0 = {'ati': "Maxsetbaev Timur", 'jasi': 20, 't_jili': 2003}
# print(student_0)
# del student_0['jasi']
# print(student_0)

# Sózlikti bir neshe qatarg'a jaziw
# telefonlar = {
#     'Timur': "iphone x",
#     'Maxset': 'galaxy s9',
#     'Alim': 'mi 10 pro',
#     'Bayram': 'nokia 3310'
#     }
# print(telefonlar['Darmen'])

# # get() metodi
# phone = telefonlar['Timur']
# print(f'Alidin tel {telefonlar["Ali"]}')

# phone = telefonlar.get('Darmen', 'Bunday Adam bizlerde joq')
# print(phone)
# phone = telefonlar.get('Timur', 'Bunday Adam bizlerde joq')
# print(phone)
# phone = telefonlar.get('Sultan')  # None joq, пустой
# print(phone)

"""=========================================================================="""

# # items() - metod "eng-elementler" perevodi
# print(telefonlar.items())

# student_0 = {'ati': "Maxsetbaev Timur", 'jasi': 20, 't_jili': 2003}
# for key, value in student_0.items():
#     print(f"gilt: {key}")
#     print(f"tusimdirme: {value} \n")

# telefonlar = {
#     'timur': "iphone x",
#     'maxset': 'galaxy s9',
#     'alim': 'mi 10 pro',
#     'bayram': 'nokia 3310'
#     }
# for key, value in telefonlar.items():
#     print(f"{key}, {value} degen telefon ustaydi ")

# .keys() metodi Sózlikti shig'aradi
# zatlar = {
#     'alma': 10000,
#     'juzum': 20000,
#     'banan': 25000,
#     'apelsin': 16000
#     }
# print(zatlar.keys())

# print('magazindegi miyweli zatlar')
# for zat in zatlar.keys():
#     print(zat.title())

# for zat in zatlar:
#     print(zat.title())

# zatlar = {
#     'kartoshka': 10000,
#     'geshir': 20000,
#     'piyaz': 25000,
#     'may': 16000
#     }
# bazarliq = ['kartoshka', 'piyaz', 'geshir', "go'sh", 'may']
# #
# # for zat in zatlar:
# #     if zat in bazarliq:
# #         print(f"{zat.title()}- {zatlar[zat]} so'm")
#
# for zat in bazarliq:
#     if zat in zatlar.keys():
#         print(f"{zat.title()}- {zatlar[zat]} so'm")
#     else:
#         print(f"{zat} joq eken")

# # sorted
# zatlar = {
#     'kartoshka': 10000,
#     'geshir': 20000,
#     'piyaz': 25000,
#     'may': 16000
#     }
# bazarliq = ['kartoshka', 'piyaz', 'geshir', "go'sh", 'may']
#
# for zat in sorted(zatlar):
#     if zat in bazarliq:
#         print(f"{zat.title()}- {zatlar[zat]} so'm")


# # .values() manisin shigaradi
# telefonlar = {
#     'timur': "iphone x",
#     'maxset': 'galaxy s9',
#     'alim': 'mi 10 pro',
#     'bayram': 'nokia 3310'
#     }
# # print(telefonlar.values())
#
# print("paydalaniwshilar tomendegi telefonlardi udtaydi")
# for tel in telefonlar.values():
#     print(tel)


# # set() bir marte qaytalanadi
# telefonlar = {
#     'timur': "iphone x",
#     'maxset': 'galaxy s9',
#     'alim': 'mi 10 pro',
#     'bayram': 'nokia 3310',
#     'karim': "iphone x",
#     'fara': 'galaxy s9',
#     'joni': 'mi 10 pro',
#     'sultan': 'nokia 3310'
#     }
#
# # print("paydalaniwshilar tomendegi telefonlardi udtaydi")
# # for tel in telefonlar.values():
# #     print(tel)
#
# print("paydalaniwshilar tomendegi telefonlardi udtaydi")
# for tel in set(telefonlar.values()):
#     print(tel)

# toys = {'ball', 'car', 'lamp', 'ball', 'bear', 'car'}


"""==========================================================="""
"""NESTING"""
car0 = {
    'model': 'lacetti',
    'color': 'aq',
    'jil': '2018',
    'cena': '12000',
    'karobka': 'avtomat'
    }

car1 = {
    'model': 'nexia 3',
    'color': 'aq',
    'jil': '2019',
    'cena': '14000',
    'karobka': 'mexanika'
    }

car2 = {
    'model': 'gentra',
    'color': 'qara',
    'jil': '2022',
    'cena': '16000',
    'karobka': 'avtomat'
    }

# car = car0
# print(f"{car['model'].title()},"
#       f"{car['color']}-svet,"
#       f"{car['jil']}-jil, {car['cena']}$")
# car = car1
# print(f"{car['model'].title()},"
#       f"{car['color']}-svet,"
#       f"{car['jil']}-jil, {car['cena']}$")
# car = car2
# print(f"{car['model'].title()},"
#       f"{car['color']}-svet,"
#       f"{car['jil']}-jil, {car['cena']}$")

cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['color']}-svet,"
#           f"{car['jil']}-jil, {car['cena']}$")

# print(cars)
# print(cars[0])
# print(cars[0]['model'])

# malibus = []
# for n in range(10):
#     new_car = {
#         'model': 'Malibu',
#         'color': None,
#         'jil': 2023,
#         'cena': None,
#         'km': 0,
#         'karobka': 'avto'
#         }
#     malibus.append(new_car)

# for malibu in malibus:
#     print(malibu)

# for malibu in malibus[:3]:
#     malibu['color'] = 'qara'
#
# for malibu in malibus[3:6]:
#     malibu['color'] = 'aq'
#
# for malibu in malibus[6:]:
#     malibu['color'] = 'qizil'
#     malibu['karobka'] = 'mexanika'
#
# # for malibu in malibus:
# #     print(malibu)
#
# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['cena'] = 40000
#     else:
#         malibu['cena'] = 35000
#
# for malibu in malibus:
#     print(malibu)


# dasturshiler = {
#     'timur': ['python', 'c++'],
#     'sultan': ['html', 'css', 'js'],
#     'bayram': ['php', 'sql'],
#     'rasul': ['python', 'php'],
#     'artur': ['c++', 'c#'],
#     }
#
# # for ati, tiller in dasturshiler.items():
# #     print(f"\n{ati.title()} tomendegi tillerdi bledi:")
# #     for til in tiller:
# #         print(til.upper())
#
# for ati, tiller in dasturshiler.items():
#     print(f"\n{ati.title()} tomendegi tillerdi bledi:")
#     for til in tiller:
#         print(f"{til.upper()}", end=" ")


# kasiplesler = {
#     "timur": {'familiya': 'maxsetbaev',
#               't_jil': 2003,
#               "maglumati": 'joqari',
#               'tiller': ['python', 'c++']},
#     "sultan": {'familiya': 'saparov',
#               't_jil': 2000,
#               "maglumati": 'joqari',
#               'tiller': ['html', 'css','js']},
#     "bayram": {'familiya': 'gjoldasbaev',
#               't_jil': 1999,
#               "maglumati": 'joqari',
#               'tiller': ['php', 'sql']}
#     }
#
# for ati, info in kasiplesler.items():
#     print(f"\n{ati.title()} {info['familiya']}, "
#           f"{info['t_jil']}-jilda tuwilgan. "
#           f"Mag'lumati: {info['maglumati']}. \n"
#           f"Tomendegi tillerdi bledi:")
#     for til in info['tiller']:
#         print(til.upper())
