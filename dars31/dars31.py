from uuid import uuid4

# class Avto:
#     """Avtomobil klasi"""
#     __num_avto =0
#     def __init__(self,make,model,color,year,cost,distance=0) :
#         self.make =make
#         self.model =model
#         self.color =color
#         self.year =year
#         self.cost =cost
#         self.__distance =distance
#         self.__id =uuid4()
#         Avto.__num_avto +=1


#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto

#     def get_distance(self):
#         return self.__distance

#     def get_id(self):
#         return self.__id

#     def add_distance(self,distance):
#         """Mashinaning km ga yana km qo'shish."""
#         if distance >= 0:
#             self.__distance += distance
#         else:
#             print("Mashina km kamaytirib bo'lmaydi. ")    

# avto1 = Avto("GM","Cobalt","Qora",2019,15000,1000)
# avto2 = Avto("Lada","Vesta","Oq",2020,16000,500)
# avto3 = Avto("Hyundai","Tucson","Qizil",2022,25000)

# print(avto1.add_distance(-2000))
# print(avto1.get_distance())
# print(avto1.get_id())
# print(avto1.get_num_avto())
# print(Avto.get_num_avto())



class Shaxs:
    """Shaxs haqidagi  ma'lumotlar"""
    num_person =0
    def __init__(self,name,lastname,passport,birthyear):
        """Shaxsning ma'lumotlari"""
        self.name =name
        self.lastname =lastname
        self.passport =passport
        self.birthyear =birthyear
        self.__id  = uuid4()

    def get_info(self):
        """Shaxs haqida ma'lumot"""  
        info = f" {self.name} {self.lastname}. "
        info += f"Passport seriyasi:{self.passport}, {self.birthyear}-yilda tug'ilgan." 
        return info

    def get_age(self,current_year =2022):
        """Shaxsning yoshini qaytaruvchi metod"""
        return current_year -self.birthyear

    def get_id(self):
        return self.__id    

inson1 = Shaxs("Hasanjon","Omonov","AC2478062",2003) 

print(inson1.get_info())
print(inson1.get_age())


class Talaba(Shaxs):
    """Talaba klasi"""
    num_students =0
    def __init__(self, name, lastname, passport, birthyear,IdNumber,Address):
        """Talabaning xususiyatlari"""
        super().__init__(name, lastname, passport, birthyear)
        self.IdNumber =  IdNumber
        self.level = 1 
        self.Address =Address
        self.subjects = []
        Talaba.num_person +=1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.IdNumber 

    def get_level(self):
        """Talabaning nechinchi kursligi"""
        return self.level   

    def get_info(self):
        """Talaba haqida ma'lumot"""  
        info = f" {self.name} {self.lastname}. "
        info += f"{self.level}-bosqich, ID raqami:{self.IdNumber}." 
        return info    

    @classmethod
    def get_num_student(Avto):
        return Avto.num_person 


class Subjects:
    """Fanlarni o'zida saqlovchi class"""
    def __init__(self,name):
        self.name = name







