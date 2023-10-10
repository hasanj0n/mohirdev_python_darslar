
# class Shaxs:
#     """Shaxs haqidagi  ma'lumotlar"""
#     def __init__(self,name,lastname,passport,birthyear):
#         """Shaxsning ma'lumotlari"""
#         self.name =name
#         self.lastname =lastname
#         self.passport =passport
#         self.birthyear =birthyear

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""  
#         info = f" {self.name} {self.lastname}. "
#         info += f"Passport seriyasi:{self.passport}, {self.birthyear}-yilda tug'ilgan." 
#         return info

#     def get_age(self,current_year =2022):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return current_year -self.birthyear

# inson1 = Shaxs("Hasanjon","Omonov","AC2478062",2003) 

# print(inson1.get_info())
# print(inson1.get_age())


# class Talaba(Shaxs):
#     """Talaba klasi"""
#     def __init__(self, name, lastname, passport, birthyear,IdNumber,Address):
#         """Talabaning xususiyatlari"""
#         super().__init__(name, lastname, passport, birthyear)
#         self.IdNumber =  IdNumber
#         self.level = 1 
#         self.Address =Address
#         self.subjects = []

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.IdNumber 

#     def get_level(self):
#         """Talabaning nechinchi kursligi"""
#         return self.level   

#     def get_info(self):
#         """Talaba haqida ma'lumot"""  
#         info = f" {self.name} {self.lastname}. "
#         info += f"{self.level}-bosqich, ID raqami:{self.IdNumber}." 
#         return info    


# class Subjects:
#     """Fanlarni o'zida saqlovchi class"""
#     def __init__(self,name):
#         self.name = name


        




# talaba1 = Talaba("Hasanjon","Omonov","AC2478062",2003,3368985,"joy")

# print(talaba1.get_id())
# print(talaba1.get_info())
# print(talaba1.get_age())


# class Address:
#     """Manzil saqlash uchun class"""
#     def __init__(self,house,street,city,region):
#         """Manzil xususiyatlari"""
#         self.house =house
#         self.street =street
#         self.city =city
#         self.region =region

#     def get_address(self):
#         """Manzilni olish"""
#         address = f"{self.region} viloyati , {self.city} shahri, "
#         address += f"{self.street} ko'chasi , {self.house}-uy. "
#         return address

# talaba2_address = Address(8,"Shamsiya","Qarshi","Qashqadaryo")
# talaba2 = Talaba("Hasanjon","Omonov","Ac2478062",2003,3368985,talaba2_address)

# print(talaba2.Address.get_address())



################################################################################################################################################################################################################33333

# from cgi import print_arguments


class Shaxs:
    """Shaxs haqidagi  ma'lumotlar"""
    def __init__(self ,name ,lastname ,passport ,birthyear):
        """Shaxsning ma'lumotlari"""
        self.name =name
        self.lastname = lastname
        self.passport = passport
        self.birthyear = birthyear

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f" {self.name} {self.lastname}. "
        info += f"Passport seriyasi:{self.passport}, {self.birthyear}-yilda tug'ilgan."
        return info

    def get_age(self, current_year=2022):
        """Shaxsning yoshini qaytaruvchi metod"""
        return current_year - self.birthyear


inson1 = Shaxs("Hasanjon", "Omonov", "AC2478062", 2003)


class Sotuvchi(Shaxs):
    """Sotuvchi haqida xususiyatlar."""

    def __init__(self, name, lastname, passport, birthyear, market, market_address):
        super().__init__(name, lastname, passport, birthyear)
        self.market = market
        self.market_address = market_address
        self.maosh = 500

    def get_info(self):
        """Sotuvchi haqidagi ma'lumot."""
        return f"Sotuvchining to'liq ismi:{self.name} {self.lastname}. U {self.market_address}da joylashgan {self.market}da ishlaydi va maoshi {self.maosh}$. "

    def set_maosh(self, maosh1):
        """Maoshni belgilab qo'yish uchun metod."""
        self.maosh = maosh1


sotuvchi1 = Sotuvchi("Jasur", "Ergashev", "JK1238954", 2002, "Baraka", "Mirzo Ulug'bek")

sotuvchi1.set_maosh(600)

print(sotuvchi1.get_info())
