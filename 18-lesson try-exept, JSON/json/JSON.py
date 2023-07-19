"""

    Python: 7-lesson

    Avtor: Darmen Allambergenov

    Tema: JSON

"""

import json
#
# x = 10
# x_json = json.dumps(x)
#
# y = 5.5
# y_json = json.dumps(y)
#
# m = True
# m_json = json.dumps(m)
#
# # ism = "Darmen"
# # ism_json = json.dumps(ism)
# # familiya_json = json.dumps('Allambergenov')
#
# sanlar = (12, 45, 23, 67)
# sanlar_json = json.dumps(sanlar)

# #
# nawqas = {
#     "ati": "Alijon Valiyev",
#     "jasi": 30,
#     "semiya": True,
#     "perzentleri": ("Bayram", "Banu"),
#     "allergiya": None,
#     "dariler": [
#         {"ati": "Analgin", "kolemi": 0.5},
#         {"ati": "Demidrol", "kolemi": 1.2},
#     ],
# }
# with open("nawqas.json", "w") as f:
#     json.dump(nawqas,f)
# nawqas_json = json.dumps(nawqas, indent=4)
# print(nawqas_json)
#


# with open("sanlar.json", "w") as f:
#     json.dump(sanlar, f)
#
# nawqas2 = json.loads(nawqas_json)
#


#
# import json
#
# filename = "nawqas.json"
# with open(filename) as f:
#     nawqas = json.load(f)
#
# print(nawqas)
# print(type(nawqas))

# import json
#
# # 1
# data = {"Model": "Malibu", "Color": "Qara", "jil": 2020, "cena": 40000}
# data_json = json.dumps(data, indent=4)
# #
# # 2
# student_json = """{"ati":"Hasan","familiya":"Husanov","tjil":2000}"""
# student = json.loads(student_json)
# print(f"{student['ism']} {student['familiya']}")
#
# # 3
# with open("data.json", "w") as f:
#     json.dump(data, f)
#
# with open("student.json", "w") as f:
#     json.dump(student, f)
#
# # 4 Students
# with open("students.json") as f:
#     data = json.load(f)
#
# for item in data["student"]:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")
#
# # 5 Wikipedia
# #
# with open("wikipedia.json") as f:
#     wiki = json.load(f)
# print(wiki)

# print(wiki["query"]["pages"]["13801"]["title"])
# print(wiki["query"]["pages"]["13801"]["extract"])

