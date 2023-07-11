"""

    Python: 7-lesson

    Avtor: Darmen Allambergenov

    Tema: INPUT() ХАМ WHILE

"""
# # input()
# ati = input("atin kim?: ")
# soraw = f"Qalay {ati.title()}. Jasin'iz neshede?"
# jas = input(soraw)
# jas = int(jas)
# height = input("Boyg'iz neshe metr?")
# height = float(height)

# # while()
# san = 1
# while san <= 5:
#     print(san, end=" ")
#     san += 1  # san = san + 1
# print('Dastur tawsildi! ')

# print("Kiritilgen sannin' kvadratin qaytariwshi dastur")
# soraw = "Qalegen san jazin'"
# soraw += "(dasturdi toxtatiw ushin 'exit' dep jazin'): "
# juwap = ' '
# while juwap != "exit":
#     juwap = input(soraw)
#     if juwap != 'exit':
#         print(float(juwap)**2)
# print('Dastur tawsildi! ')

# Belgi
# print("Kiritilgen sannin' kvadratin qaytariwshi dastur")
# soraw = "Qalegen san jazin'"
# soraw += "(dasturdi toxtatiw ushin 'exit' dep jazin'): "
# belgi = True
# while belgi:
#     juwap = input(soraw)
#     if juwap == 'exit':
#         belgi = False
#     else:
#         print(float(juwap)**2)
# print('Dastur tawsildi! ')

# # break
# print("Kiritilgen sannin' kvadratin qaytariwshi dastur")
# soraw = "Qalegen san jazin'"
# soraw += "(dasturdi toxtatiw ushin 'exit' dep jazin'): "
#
# while True:
#     juwap = input(soraw)
#     if juwap == 'exit':
#         break
#     else:
#         print(float(juwap)**2)
# print('Dastur tawsildi! ')

# sanlar = list(range(1, 11))
# for san in sanlar:
#     if san == 5:
#         break
#     print(f"{san} kvadtari {san**2} boladi")

# # CONTINUE
# sanlar = list(range(1, 11))
# for san in sanlar:
#     if san == 5:
#         continue
#     print(f"{san} kvadtari {san**2} boladi")

# # CONTINUE while
# san = 0
# while san < 10:
#     san += 1
#     if san % 2 == 0:
#         continue
#     else:
#         print(san)

# infinite loop qatelik
# san = 0
# while san < 10:
#     san += 1
#     if san % 2 == 0:
#         continue
#     else:
#         print(san)

# san = 0
# while san < 10:
#     san += 1
#     if san % 2 == 0:
#         continue
#     else:
#         print(san)

# san = 1
# while san > 0:
#     san += 1
#     if san % 2 == 0:
#         continue
#     else:
#         print(san)

# """==========================================================="""

# print("Jaqin doslardin dizimi")
# atlar = []
# n = 1  # atlardi sanaw ushin ozgeriwshi
# while True:
#     soraw = f"{n}) dostin'izdin atin jazin?: "
#     ati = input(soraw)
#     atlar.append(ati)
#     qaytalaw = input("jane dos qosasizba? (yaq/awa)")
#     n += 1
#     if qaytalaw == 'yaq':
#         break
#
# print("Doslarinizdin dizimi:")
# for at in atlar:
#     print(at.title())

# doslar = {}
# belgi = True
# while belgi:
#     ati = input("Dostinizdin atin jazin?")
#     jas = input(f"{ati.title()} neshe jasta?: ")
#     doslar[ati] = int(jas)
#
#     juwap = input("jane mag'lumat qosasizba?(awa/yaq): ")
#     if juwap == 'yaq':
#         belgi = False
#
# for ati, jasi in doslar.items():
#     print(f"{ati.title()} {jasi}-jasda.")
# print(doslar)

# cars = ['lacetti', 'nexia', 'tayota', 'nexia', 'audi', 'malibu', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)
#
# cars = ['lacetti', 'nexia', 'tayota', 'nexia', 'audi', 'malibu', 'nexia']
# car = 'nexia'
# while car in cars:
#     cars.remove(car)
# print(cars)

# studentler = ['timur', 'maxset', 'sultan', 'artur']
# bahalangan_studentler = {}
# while studentler:
#     student = studentler.pop()
#     baha = input(f"{student.title()} neshe baha aldi?: ")
#     print(f"{student} bahalandi!\n")
#     bahalangan_studentler[student] = int(baha)
#
# print(studentler)
# print(bahalangan_studentler)

kitaplar = []
while True:
    kitap = input("jaqsi korgen kitapti jazin(programma toqtaw ushin (stop)): ")
    if kitap.lower() == "stop":
        break
    else:
        kitaplar.append(kitap)
print("Programma toxtadi")
print("sizdin jaqsi korgen kitaplariniz", kitaplar)






