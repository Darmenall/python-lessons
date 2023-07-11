"""

    Python: 13-lesson

    Avtor: Darmen Allambergenov

    Tema:  (OOP) Object Oriented Programming

"""

############ Klassik Dasturlew (Siziqli Dasturlew)###############

# a = int(input("a: "))
# b = int(input("b: "))
# c = (a**2) + (2*a*b) + (b**2)
# print(c)



############## OOP klasslari ##############
#
# x = 10
# print(type(x))
#
#
# text = "hello"
# print(type(text))


################ metod ###############

# print(text.upper())
# print(x.upper())
#
# def hi():
#     print("Assalamu aleykum")
#
# print(type(hi))

################# obekt jaratiw #############

# class Student: # class (obekt ushin shablom)
#     def __init__(self, ati, familiyasi, jasi):
#         self.ati = ati  # kassietleri
#         self.familiya = familiyasi
#         self.jasi = jasi
#
# student1 = Student("Artur", "AStanov", 2004)  # obekt
#
# student1.ati
# student1.jasi
# student1.familiya
#
# student2 = Student("Rasul", "Aydabullaev", 2003)
# student3 = Student("Bayram", "djoldasbaev", 1999)



################# klasstin metod #####################

# class Student:  # class (obekt ushin shablom)
#     def __init__(self, ati, familiyasi, t_jil):
#         self.ati = ati  # kassietleri
#         self.familiya = familiyasi
#         self.t_jil = t_jil
#
#     def tanistir(self):  # medot
#         print(f"Men {self.ati.title()} {self.familiya.title()} jasim {self.t_jil}")  # Duris emes nejizi
#         return f"Men {self.ati.title()} {self.familiya.title()} jasim {self.t_jil}"
#
#     def get_name(self):
#         return self.ati
#
#     def get_lastname(self):
#         return self.familiya
#
#     def get_age(self, jil):
#         return jil - self.t_jil
#
#     def get_tjil(self):
#         return self.t_jil
#
# student1 = Student("Artur", "AStanov", 2004)

############################################################

class Student: # class (obekt ushin shablom)
    def __init__(self, ati, familiyasi, t_jil): # parametrleri
        self.ati = ati  # kassietleri
        self.familiya = familiyasi
        self.t_jil = t_jil
        self.kurs = 1


    def get_info(self):  # medot
        # print(f"Men {self.ati.title()} {self.familiya.title()} jasim {self.t_jil}")  # Duris emes nejizi
        return f"Men {self.ati.title()} {self.familiya.title()} jasim {self.t_jil} , {self.kurs}-studentimen"

    def get_name(self):
        return self.ati

    def get_lastname(self):
        return self.familiya

    def get_age(self, jil):
        return jil - self.t_jil

    def get_tjil(self):
        return self.t_jil

    def get_kurs(self):
        return self.kurs

#########################################

    def set_kurs(self, taza_kurs):
        self.kurs = taza_kurs
        return self.kurs

    def update_kurs(self):
        self.kurs += 1
        return self.kurs



# student1 = Student("Artur", "AStanov", 2004)
# # student1.kurs
#
# student1.kurs = 2
# student1.get_kurs()

class Pan:
    def __init__(self, ati):
        self.ati = ati
        self.studentler_sani = 0
        self.studentler = []

    def add_student(self, student):
        self.studentler.append(student)
        self.studentler_sani += 1

    ######### konsol #########
    # student1 = Student("Artur", "AStanov", 2004)
    # student2 = Student("Rasul", "Aydabullaev", 2003)
    # fizika = Pan("fizika")
    # fizika.studentler_sani
    # fizika.studentler
    # fizika.add_student(student1)
    # fizika.add_student(student2)
    # fizika.studentler
    # fizika.studentler[0].ati
    # fizika.studentler[1].get_info()
    ##################################
    def get_name(self):
        return self.ati

    def get_students(self):
        return [x.get_info() for x in self.studentler]

    def get_studentler_sani(self):
        return self.studentler_sani

    ######## metod qasyetlerin koriw ##############
    # dir(Student) # klasstin methodlarin qaytaradi
    #
    # def see_methods(klass):
    #     return [method for method in dir(klass) if not method.startswith('__')]
    #
    # student1.__dict__ # gilt b-n sogan tiysli manislerin qaytaradi


