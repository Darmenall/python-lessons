"""

    Python: 7-lesson

    Avtor: Darmen Allambergenov

    Tema:Sirtqi moduller
"""
# import requests
# from bs4 import BeautifulSoup
#
#
# bet = "https://kun.uz/news/main"
# r = requests.get(bet)
# # pprint(r.text)
#
# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup.prettify())
# news = soup.find_all(class_="news-title")
# print(news[0].text)

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

# # Eki so'z ortasindagi kusasliqtin % aniqlaw
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))

# Text arasindag'i 3  eng kusasin ajratip aliw
# text = "салом"
# matches = process.extract(text, words, limit=3)
# print(matches)

# # Text arasindag'i eng kusasin tawi
# text = "талба"
# match = process.extractOne(text, words)
# print(match)


# # pip install googletrans==3.1.0a0
# from googletrans import Translator
#
# tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
#
# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
#
# # Istalgan matnni ingliz tiliga tarjima qilish uchun tranlsate metodini chariqamiz
# tarjima = tarjimon.translate(matn_uz)
# # Original matn
# # print(tarjima.origin)
# # # Tarjima
# # print(tarjima.text)
# # # Original matn tili
# # print(tarjima.src)
#
# # # Boshqa tilga tarjima qilish uchun dest parametridan foydalanamiz
# tarjima_ru = tarjimon.translate(matn_uz, dest="ru")
# # print(tarjima_ru.text)
#
# # # Ingliz tilidan tarjima
# matn_en = "Tashkent is the capital of Uzbekistan"
# tarjima_uz = tarjimon.translate(matn_en, dest="uz")
# print(tarjima_uz.text)


