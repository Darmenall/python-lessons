"""

    Python: 11-lesson

    Avtor: Darmen Allambergenov

    Tema:  *args ha'm **kwargs

"""
# def summa(*sanlar):
#     jiyndi = 0
#     for san in sanlar:
#         jiyndi += san
#     return jiyndi

# #
# # # def summa(*sanlar):
# # #     return sum(sanlar)
# #
# #
# print(summa(1))
# print(summa(1, 2, 3, 4, 5))
# print(summa(5, 6, 7))

#
def summa(x, y, *sanlar):
    return x+y+sum(sanlar)


print(summa(1, 2))
print(summa(1, 2, 3, 4, 5))
print(summa(5, 6, 7))



# # **kwards
#
def avto_info(kompaniya, model, **malumatlar):
    malumatlar['kompaniya'] = kompaniya
    malumatlar['model'] = model
    return malumatlar

#
avto1 = avto_info("Gm", 'malibu', color='qara', jil=2018)
avto2 = avto_info("Kia", 'k5', color='aq', jil=2023)
#
print(avto1)
print(avto2)










