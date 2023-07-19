"""

    Python: 7-lesson

    Avtor: Darmen Allambergenov

    Tema:try-except

"""
## Qateler
# jas = input("Jasinizdi kiritin': ")
# jas = int(jas)
# print(f"Siz {2021-jas} jilda tuwilg'an ekensiz")

# try-except
# jas = input("Jasinizdi kiritin': ")
# try:
#     jas = int(jas)
#     print(f"Siz {2021-jas} jilda tuwilg'an ekensiz")
# except:
#     print("putun san jazin'!")

## try-except-else
# print("Dastur Tawsildi!")
# jas = input("Jasin'izdi kiritin': ")
# try:
#     jas = int(jas)
# except ValueError:
#     print("putun san jazin'")
# else:
#     print(f"Siz {2023-jas} jilda tuwilg'an ekensiz")

# x,y=5,10
# try:
#    y/(x-5)
# except ZeroDivisionError:
#     print("0 ge bolinbiydi")

# miweler = ['alma','anar','anjir','juzum']
# try:
#     print(miweler[7])
# except IndexError:
#     print(f"dizimde {len(miweler)}  miwe bar tek")

# user = {"username":"Texno-park",
#         "status":"admin",
#         "email":"@darmen_all",
#         "phone":"906545438"}
#
# key="tel"
# try:
#     print(f'Paydalaniwshi: {user[key]}')
# except KeyError:
#     print("Bunday giltso'z So'zlikte joq")

# filename = "data.txt" # bunday fail joq!
# with open(filename) as f:
#     text = f.read()

# filename = "data.txt" #  bunday fail joq!
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Keshirersiz, {filename} fayli tawalmadim. Bos fayl tan'la.")

# n = input("Putun san kiritin': ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError:
#     print("Putun san kiritilmedi")
# except ZeroDivisionError:
#     print("0 ge bo'lib bo'lmaydi")
# else:
#     pass

# import json
# files = ['student1.json','student2.json','student3.json','student4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             student = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} fail joq!")
#     else:
#         print(student['ati'])
#         # fayl ustinde turli ameller

# import json
# files = ['student1.json','student2.json','student3.json','student4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             student = json.load(f)
#     except FileNotFoundError:
#         pass
#     else:
#          print(student['ati'])
#         # fayl ustinde turli ameller


