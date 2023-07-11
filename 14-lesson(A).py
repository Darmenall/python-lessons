"""

    Python: 14-lesson

    Avtor: Darmen Allambergenov

    Tema:  NASIL ha'm POLIMORFIZM

"""

# class Adam:
#     """Adam qaqinda magliwmat"""
#     def __init__(self, ati, familiyasi, passport, tjil):
#         """Adamnin' qasiyetleri"""
#         self.ati = ati
#         self.fam = familiyasi
#         self.passport = passport
#         self.tjil = tjil

#     def get_info(self):
#         """Adam qaqinda mag'liwmat"""
#         info = f"{self.ati} {self.fam}. "
#         info += f"Passport {self.passport}, {self.tjil}- jili tiwilg'an"
#         return info

#     def get_age(self, jil):
#         """Adamnin' jasin qaytariwshi metod"""
#         return jil - self.tjil


# class Student(Adam):
#     """Student klassi"""
#     def __init__(self, ati, familiyasi, passport, tjil, idnomer):
#         """Studenttin' qasiyetleri"""
#         super().__init__(ati, familiyasi, passport, tjil)
#         self.idnomer = idnomer
#         self.kurs = 1

#     def get_id(self):
#         """Studentin' ID nomeri"""
#         return self.idnomer

#     def get_kurs(self):
#         """Studenttin' kursi"""
#         return self.kurs

# # =============================================================================
# #     ############# Polimorfizm ##############
# # =============================================================================

#     def get_info(self):
#         """Student haqinda mag'liwmat"""
#         info = f"{self.ati} {self.fam}. "
#         info += f"{self.tjil}- jili tiwilg'an, {self.kurs}-kurs ID-{self.idnomer}"
#         return info


# =============================================================================
# biz klassga qandayda qasiyetler kosuwmis mumkin ha'm kasiyetleri dim kobeyp
# ketiw mumkin ha'm bul bizdin obektimizdin duris islewi yamasa obektke
# murajat kiliwdi qiynlastirip jberiw mumkin
# =============================================================================


class Adam:
    """Adam qaqinda magliwmat"""
    def __init__(self, ati, familiyasi, passport, tjil):
        """Adamnin' qasiyetleri"""
        self.ati = ati
        self.fam = familiyasi
        self.passport = passport
        self.tjil = tjil

    def get_info(self):
        """Adam qaqinda mag'liwmat"""
        info = f"{self.ati} {self.fam}. "
        info += f"Passport {self.passport}, {self.tjil}- jili tiwilg'an"
        return info

    def get_age(self, jil):
        """Adamnin' jasin qaytariwshi metod"""
        return jil - self.tjil


class Student(Adam):
    """Student klassi"""
    def __init__(self, ati, familiyasi, passport, tjil, idnomer, manzil):
        """Studenttin' qasiyetleri"""
        super().__init__(ati, familiyasi, passport, tjil)
        self.idnomer = idnomer
        self.kurs = 1
        self.manzil = manzil

    def get_id(self):
        """Studentin' ID nomeri"""
        return self.idnomer

    def get_kurs(self):
        """Studenttin' kursi"""
        return self.kurs

# =============================================================================
#     ############# Polimorfizm ##############
# =============================================================================

    def get_info(self):
        """Student haqinda mag'liwmat"""
        info = f"{self.ati} {self.fam}. "
        info += f"{self.tjil}- jili tiwilg'an, {self.kurs}-kurs ID-{self.idnomer}"
        return info

class Manzil:
    def __init__(self, uy, koshe, qala):
        self.uy = uy
        self.koshe = koshe
        self.qala = qala

    def get_manzil(self):
        manzil = f"{self.qala} - qalasinda, {self.koshe} - koshesi, {self.uy} - uy"
        return manzil

student1_manzil = Manzil(1, "Tilek", "No'kis")
student1 = Student("Darmen", "Allambergenov", "KA092113", 2000, "NO12044", student1_manzil)

student1.manzil
# student1.manzil.get_manzil()










