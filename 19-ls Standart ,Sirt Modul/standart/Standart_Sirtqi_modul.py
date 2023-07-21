"""
03/02/2021

    Python: 6-lesson

    Avtor: Darmen Allambergenov

    Tema: Standart, Sirtqi moduller

"""
# import datetime as dt
#
# # datetime()
# kazir = dt.datetime.now()
# print(kazir)
# # Saneni ajratip aliw
# print(kazir.date())
# # Waqitti ajratip aliw
# print(kazir.time())
# # Sag'atti ajratip aliw
# print(kazir.hour)
# # Minutti ajratip aliw
# print(kazir.minute)
# # sekundni ajratip aliw
# print(kazir.second)
#
# # date()
# bugin = dt.date.today()
# print(f"Bugungi sane: {bugin}")
# erten = dt.date(2021, 3, 10)
# print(f"Ertengi sane: {erten}")
#
# # time()
# kazir = dt.datetime.now()
# vaqtkazir = kazir.time()
# print(f"Hozir soat: {vaqtkazir}")
# vaqtKeyin = dt.time(23, 45, 30)
# print(vaqtKeyin)
#
# # saneler arasindagi parx
# bugin = dt.date.today()
# ramazan = dt.date(2021, 4, 13)
# parx = ramazan - bugin
# # print(farq)
# print(f"Ramazanga {parx.days} ku'n qaldi")
#
# # # Sag'atlar arasindagi parx
# kazir = dt.datetime.now()
# futbol = dt.datetime(2021, 3, 10, 23, 45, 00)
# parx = futbol - kazir
# sekundlar = parx.seconds
# minutlar = int(sekundlar / 60)
# sagatlar = int(minutlar / 60)
# print(f"Futbol baslaniwna {parx.days} kun {sagatlar} sag'at qaldi")
#
# # Waqitti formatlaw
# waqit = kazir.strftime("%H:%M:%S")
# print(f"kazir sag'at: {waqit}")
#
# sane = kazir.strftime("%d-%m-%Y")
# print(f"Bugin sane: {sane}")
#
# sane_vaqt = kazir.strftime("%d/%m/%Y, %H:%M")
# print(sane_vaqt)

############################### Math #################################

import math

# PI = math.pi
# # print(f"PI din' manisi: {PI}")
# # E = math.e
# # print(f"e nin' manisi: {E}")
#
# # # trigonometriya
# math.sin(math.pi / 2)
# math.cos(0)
# math.tan(PI)


# # # logarifmler
# # natural logarifm
# math.log(5)
# # 10 liq logarifm
# math.log10(100)

# # Sonlardi domalaklaw
# x = 4.6
# print(math.ceil(x))
# print(math.floor(x))

# # Kvadrat koren
# x = 81
# math.sqrt(x)
#
# # Dareje
# math.pow(x, 3)  # x din' kubi
# math.pow(x, 5)  # x din' 5-darejesi
# math.pow(x, 1 / 3)  # x din' kub koreni
#
########################### pprint #################################################

from pprint import pprint
import json
#
# filename = "nawqas.json"
# with open(filename) as f:
#     nawqas = json.load(f)
#
# # pprint(nawqas)
# pprint(nawqas)

# import requests
#
# r = requests.get("https://api.github.com")
# #
# # pprint(r.json())
# # print(r.json())


