"""

    Python: 11-lesson

    Avtor: Darmen Allambergenov

    Tema:  Moduller

"""
import math
# from 11-lesson import summa, avto_info
# from 11-lesson import summa as sm , avto_info as av
#
# print(summa(1,2,3,4,5))
# avto = avto_info('Gm', 'Malibu', color="qara", jil=2019, cena=23000)
# print(avto)
#
#
# import 10-lesson
# salem_ber('Artur')

# import math
# # x = 400
# # print(math.sqrt(x))
# # print(math.pow(5, 3))
# # print(math.pi)
# # print(math.log10(100))
#
import random as r

# # san = r.randint(0, 100)
# # print(san)
#
# atlar = ['Artur', 'Anvar', 'Rasul', 'Bayram']
# # ati = r.choice(atlar)
# # print(ati)
#
# print(r.choice(atlar))

# x = list(range(0, 100, 5))
# print(x)
# print(r.choice(x))

# # shufle()
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# ===========================Lambda=========================================

# def ati(argument):
#     return manis

# lambda argument1, argument2: manis=argument1+argument2
# uzunliq - Idintifikator
#
# uzunliq = lambda pi, r : 2*pi*r
# print(uzunliq(math.pi,10))
#
# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))

# def dareje(n):
#     return lambda x : x**n
#
# kvadrat = dareje(2)
# kub = dareje(3)
# print(f"3tin kvadrati {kvadrat(3)} ge ten', "
#       f"kubi {kub(3)} ge ten'")

from math import sqrt

# sanlar = list(range(11))
# korenler = list(map(sqrt,sanlar))
# print(korenler)

# def dareje2(x):
#     return x*x
#
# print(list(map(dareje2, sanlar)))

# kvadratlar = list(map(lambda x: x*x, sanlar))
# print(kvadratlar)

# kvadrat = []
# for san in sanlar:
#     kvadrat.append(san*san)
# print(kvadrat)

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y: x+y, a, b))
# print(a_plus_b)

import random as r
# sample()
# sanlar = r.sample(range(100),10)
# print(sanlar)
# # def jup(x):
# #     return x%2==0
# # # filter()
# # jup_sanlar = list(filter(jup, sanlar))
# # print(jup_sanlar)
#
# jup_sanlar = list(filter(lambda san: san%2==0, sanlar))
# print(jup_sanlar)

# miywler = ['alma', 'juzum', 'banan', 'almurt', 'garbiz', 'ananas', 'kivi']
# harb = 'b'
# miyweler_b = list(filter(lambda miywe : miywe.startswith(harb), miywler))
# print(miyweler_b)
#
# miywler2 = list(filter(lambda miywe: len(miywe)<=5, miywler))
# print(miywler2)

sanlar = r.sample(range(100), 10)
print(sanlar)

jup = [san for san in sanlar if san%2==0]
print(jup)

print([san for san in sanlar if san%2==0])






