"""

    Python: 6-lesson

    Avtor: Darmen Allambergenov

    Tema: IF-ELSE

    ==, !=, <, >, <=, >=
"""
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ati = 'Ali'
# ati.lower() == 'ali'
#
# ati = input('atindi jaz: ')
# if ati.lower() != 'darmen':
#     print(f'Keshiresiz {ati.title()}, men Darmendi kutip atirman')
# else:
#     print('Qalay Darmen )')

# juwap = float(input('12x6 neshe boladi?: '))
# if juwap != 72:
#     print('juwap Naduris')

# jas = int(input("Jasin'iz neshede?: "))
# if jas >= 18:
#     print('Xosh kelibsiz')
# else:
#     print('Kiriw mumkin emes!')

# login = input('login: ')
# if len(login) > 6:
#     print('login duris ashildi')
# else:
#     print("Iltimas logindi 6 simvoldan kop etip jazin'")


# t_jil = int(input("tuwilgan jilin'iz neshede?: "))
# if 2023-t_jil>=16:
#     print("Xosh kelibsiz")
# else:
#     print(f"Sizdin jasiz {2023-t_jil} eken.")
#     print("Sizge ushiwga bolmaydi!")

# jas = int(input("Tuwilgan jilin'izdi jazin: "))
# if jas > 65: print("Siz COVID-19 risk gruppasinda ekensiz!")

# x, y = 25, 50
# print("x>y") if x > y else print('x<y')













# san = -50
# if san < 0:
#     print('teris san')
# else:
#     print("on' san")

# san = int(input("San jaz: "))
# if san < 0:
#     print('teris san')
# elif san == 0:
#     print("on' sanda, teris sanda emes 0 ge ten'")
# else:
#     print("on' san")

# jasi = int(input("Jasin'izdi  jazin: "))
# if jasi <= 4:
#     print('Sizge kiriw bipul')  # cena = 0
# elif jasi <= 12:
#     print("Sizge kiriw 5000 so'm")   # cena = 5000
# else:
#     print("Sizge kiriw 10000 so'm")  # cena = 10000
# print(f"sizge kiriw {cena}")

# for i in range(3):
#     jasi = int(input("Jasin'izdi  jazin: "))
#     if jasi <= 4:
#         print('Sizge kiriw bipul')
#     elif jasi <= 12:
#         print("Sizge kiriw 5000 so'm")
#     else:
#         print("Sizge kiriw 10000 so'm")

"""
    OR, AND-operatori
"""
# kun = input("bugin neshinshi kun?: ")
# if kun.lower() == "6" or kun.lower() == 'qalakun':
#     print("Bugin dem aliw kuni")
# else:
#     print('Harma')

# kun = input("bugin neshinshi kun?: ")
# temp = float(input('pagoda neshe gradus?: '))

# if kun.lower() == "qalakun" and temp > 30:
#     print("Kettik shomiliwga ;)")
# elif kun.lower() == "qalakun" and temp < 30:
#     print("Uyde dem alamis")

# if (kun.lower() == "6" or kun.lower() == 'qalakun') and temp > 30:
#     print("Kettik shomiliwga ;)")
# elif (kun.lower() == "6" or kun.lower() == 'qalakun') and temp < 30:
#     print("Uyde dem alamis")

# cena = 15000
# shay = True
# salat = True
#
# if shay and salat:
#     cena += 10000
# elif shay or salat:
#     cena += 5000
# print(cena)

# cena = 15000
# shay = 1
# salat = 0
# nan = 1
# kampot = 1
#
# if shay:
#     cena += 5000
#     print(f"klient shay aldi")
# if salat:
#     cena += 5000
#     print(f"klient salat aldi")
# if nan:
#     cena += 5000
#     print(f"klient nan aldi")
# if kampot:
#     cena += 5000
#     print(f"klient kampot aldi")
# print(f"obshi summa {cena} boldi")

# menu = ['palaw', 'gurtik', 'shawle', 'narin', 'somsa']
# 'manti' in menu
#
#           # not in
#
# menu = ['palaw', 'gurtik', 'shawle', 'narin', 'somsa']
# awqat = input("Qanday awqat jiysiz?: ")
# if awqat.lower() in menu:
#     print("byurpa qabil qilindi")
# else:
#     print("Keshirersiz, onday awqat menuda joq!")

# menu = ['palaw', 'gurtik', 'shawle', 'narin', 'somsa']
# byurpalar = ['palaw', 'somsa', 'manti', 'shashlik']
#
# if byurpalar:
#     for awqat in byurpalar:
#         if awqat in menu:
#             print(f"Menuda {awqat} bar")
#         else:
#             print(f"Keshirersiz, {awqat} bizlerdin menuda joq!")










