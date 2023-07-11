"""

    Python: 10-lesson

    Avtor: Darmen Allambergenov

    Tema:  FUNCTIONS (FUNKCIYALAR)

"""
# print("Hello World!")
# x = 20
# print(type(x))
# print(list(range(1,11)))

# def salem_ber():
#     """salem beriwshi function"""
#     print("Assalamu Aleykum!")
#
# salem_ber()

# def salem_ber(ati):  # parametr
#     """Paydalaniwshinin' atin qaytarati,
#     salem beriwshi function"""
#     print(f"Assalamu Aleykum!, Hurmetli {ati.title()}!")
# #
# # salem_ber('artur')  # argument
# # salem_ber('bayram')
# # print(salem_ber.__doc__)
# print(print.__doc__)


# def toliq_ati(ati, familiyasi):
#     """Paydalaniwshinin' atin ha'm familiyasin qaytarati"""
#     print(f"Paydalaniwshinin' ati: {ati.title()}\n"
#           f"Paydalaniwshinin' familiyasi: {familiyasi.title()}")
#
# toliq_ati("artur", "astanov")
# # toliq_ati("astanov", "artur")

# def jas_esaplaydi(ati, tuwilgan_jili):
#     """ Paydalaniwshinin' atin ha'm jasin qaytaradi """
#     print(f"{ati.title()} {2023-tuwilgan_jili} jasda")
# #
# # jas_esaplaydi("bayram", 1999)
# # # jas_esaplaydi(1999, "bayram")
#
# jas_esaplaydi(tuwilgan_jili=1999, ati="bayram")

# def jas_esaplaydi(tuwilgan_jili, kazirgi_jil=2023):
#     """ Paydalaniwshinin' jasin qaytaradi """
#     print(f"Siz {kazirgi_jil-tuwilgan_jili} jasdasiz")
#
# jas_esaplaydi(1999,2023)
# jas_esaplaydi(1999)

# # """====================================================="""

# def toliq_ati(ati, familiyasi):
#     """Paydalaniwshinin' atin ha'm familiyasin qaytarati"""
#     at_fam = f"{ati.title()} {familiyasi.title()}"
#     print(at_fam)
#
# toliq_ati("sultan", 'saparniyazov')
# print(at_fam)

# def toliq_ati(ati, familiyasi):
#     """Paydalaniwshinin' atin ha'm familiyasin qaytarati"""
#     at_fam = f"{ati.title()} {familiyasi.title()}"
#     return at_fam
#
# # toliq_ati("sultan", 'saparniyazov')
# # print(at_fam)
#
# # student = toliq_ati("sultan", 'saparniyazov')
# # print(student)
#
# student1 = toliq_ati("sultan", 'saparniyazov')
# student2 = toliq_ati("rasul", 'aydabullaev')
# print(f"sabaqqa kelmegen studentler: {student1} ha'm {student2}")
# print(f"{student1} sabaqqa keshigip keldi")

# def toliq_ati(ati, familiyasi, ocheltvasi= ""):
#     if ocheltvasi:
#         at_fam = f"{ati} {familiyasi} {ocheltvasi}"
#     else:
#         at_fam = f"{ati} {familiyasi}"
#     return at_fam.title()
#
# student1 = toliq_ati("sultan", 'saparniyazov')
# student2 = toliq_ati("rasul", 'aydabullaev', 'paraxatovich')
# print(f"sabaqqa kelmegen studentler: {student1} ha'm {student2}")

# def avto_info(kompaniya, model, color, karobka, jili, cena = None):
#     avto ={
#         'kompaniya': kompaniya,
#         'model': model,
#         "color": color,
#         "karobka": karobka,
#         "jili": jili,
#         "cena": cena
#         }
#     return avto
#
# avto1 = avto_info('GM', 'Malibu', 'Qara', 'Avtomat',2018)
# avto2 = avto_info('GM', 'Gentra', 'Aq', 'Mexanik',2020,21000)
# avtolar = [avto1, avto2]
# print("Online bazardagi mashinlar:")
# for avto in avtolar:
#     if avto['cena']:
#         cena = avto['cena']
#     else:
#         cena = 'Belgisiz'
#     print(f"{avto['color']} {avto['model']}. Cenasi: {cena}")

# list(rande(0, 10)
# def araliq(min,max):
#     sanlar = []
#     while min<max:
#         sanlar.append(min)
#         min += 1
#     return sanlar
# print(araliq(0, 10))
# print(araliq(10, 21))
# sanlar = araliq(100,151)
# print(sanlar)  # adim degen parametr qosin'


# def avto_info(kompaniya, model, color, karobka, jili, cena = None):
#     avto ={
#         'kompaniya': kompaniya,
#         'model': model,
#         "color": color,
#         "karobka": karobka,
#         "jili": jili,
#         "cena": cena
#         }
#     return avto
#
# print("Online bazardagi mashinlar:")
# avtolar = []
# while True:
#     print("\nTomendegi maglumatlardi kiritin: ", end=" ")
#     kompaniya = input("Islep shigariwshi kompaniya: ")
#     model = input("Modeli: ")
#     color = input("Color: ")
#     karobka = input("Karobka: ")
#     jili = input("Jili: ")
#     cena = input("Cena: ")
#
#     avtolar.append(avto_info(kompaniya, model, color, karobka, jili, cena))
#
#     juwap = input("Jane mag'lumat qosasizba?(awa\yaq)")
#     if juwap == 'yaq':
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['cena']:
#         cena = avto['cena']
#     else:
#         cena = 'Belgisiz'
#     print(f"{avto['color']} {avto['model']}. Cenasi: {cena}")

# """============================================================="""
#
# def bahalaw(atlar):
#     bahalar = {}
#     while atlar:
#         at = atlar.pop()
#         baha = input(f"{at.title()} baha qoyin: ")
#         bahalar[at] = int(baha)
#     return bahalar
# studentler = ['bayram', 'rasul', "artur", 'sultan']
# bahalar = bahalaw(studentler)
# # print(bahalar)
# # print(studentler)














