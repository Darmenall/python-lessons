"""

    Python: 17-lesson

    Avtor: Darmen Allambergenov

    Tema: FILES

"""

file = open('PI.txt')
PI = file.read()
print(PI)
file.close()


# with open('PI.txt') as file:
#     pi = file.read()

# print(pi)
# pi = pi.rstrip()
# pi = pi.replace('\n', "")
# pi = float(pi)
# print(pi)


# filename = 'python\studentler.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)


# with open(filename) as file:
#     studentler = file.readlines()

# # print(studentler)


# studentler = [student.rstrip() for student in studentler]
# print(studentler)


# fileati = 'new_file.txt'
# ati = "Artur Astanov"
# tjil = 2004
# with open(fileati, 'w') as fayl:
#     fayl.write(ati)
#     fayl.write(str(tjil))


# fileati = 'new_file.txt'
# ati = "Artur Astanov"
# tjil = 2004
# with open(fileati, 'w') as fayl:
#     fayl.write(ati+'\n')
#     fayl.write(str(tjil)+'\n')


# fileati = 'new_file.txt'
# with open(fileati, 'a') as fayl:
#     fayl.write('Darmen Allambergenov\n')
#     fayl.write('2000')


# import pickle

# student1 = {'ati':'Artur', 'fam':'Astanov', 'tjil':'2004', 'kurs':'2'}
# student2 = {'ati':'Darmen', 'fam':'Allambergenov', 'tjil':'2000', 'kurs':'2'}

# # wb-write binary EKILIK SANAQ SISTEMASI
# with open('info', 'wb') as file:
#     pickle.dump(student1, file)
#     pickle.dump(student2, file)


# with open('info', 'rb') as file:  # read binary
#     student1 = pickle.load(file)
#     student2 = pickle.load(file)

# print(student1)
# print(student2)





