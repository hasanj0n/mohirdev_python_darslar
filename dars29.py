
# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.level = 1

#     def get_name(self):
#         return self.ism
#     def get_lastname(self):
#         return self.familiya

#     def get_age(self,yil=2022):
#         return yil-self.tyil

#     def set_level(self,new_level):
#         self.level = new_level

#     def update_level(self):
#         self.level += 1

#     def get_level(self):
#         return self.level    


#     def tanishtir(self):
#          return (f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil} yil. ")

#     def get_info(self):
#          return (f"Ismim {self.ism} {self.familiya},  {self.level}-bosqich talabasiman. ")


# talaba1 = Talaba("Hasanjon","Omonov",2003)
# talaba2 = Talaba("Istam","Nazirov",2004)

# # print(talaba1.get_level())
# # (talaba1.set_level(2))
# # print(talaba1.get_level())
# # (talaba1.update_level())
# # print(talaba1.get_level())
# # print(talaba1.get_info())


# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,name):
#         self.name = name
#         self.numberStudents = 0
#         self.students = []

#     def add_students(self,talaba):
#         """Fanga talabalar qo'shish"""  
#         self.students.append(talaba)  
#         self.numberStudents +=1

#     def get_students(self):
#         """Fanga yozilgan talabalar ro'yhati""" 
#         return [x.get_lastname() for x in self.students]

#     def get_students_num(self):
#         "Fanga yozilgan studentlar soni"
#         return self.numberStudents       

# subject1 =Fan("math")
# subject1.add_students(talaba1)   
# subject1.add_students(talaba2)   
# print(subject1.get_students())     
# print(subject1.get_students_num())     
# print(subject1.students[0].get_info())

"""Class ichidagi metodlarni ko'rish"""
# print(dir(Talaba)) 

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__')]

# print(see_methods(talaba1))
# print(talaba1.__dict__)





#####################################################################################################################################################################################################################################################################################################################################################






class Avto():
    def __init__(self,model,color,engine,cost,year):
        self.model =model
        self.color =color
        self.engine =engine
        self.cost =cost
        self.year =year
        self.distance = 0


    def get_name(self):
        return self.model

    
    def get_info(self):
        return f"{self.color.capitalize()} rangli mashinaning modeli:{self.model}, {self.year}-yilda ishlab chiqarilgan.Dvigateli {self.engine} va {self.cost}$. {self.distance}km yurgan. "     

    def update_distance(self):
        self.distance += 1000   

avto1 = Avto("malibu","qora","avtomat",15000,2021)
avto2 = Avto("tracker","oq","avtomat",20000,2022)
avto3 = Avto("cobalt","choco","mexanika",12000,2020)


# print(avto3.get_info())
# avto3.update_distance()
# print(avto3.get_info())


class AvtoSalon():
    def __init__(self,name,address):
        self.address = address
        self.name = name
        self.cars = []
        self.cars_num = 0


    def add_cars(self,car):
        self.cars.append(car)
        self.cars_num +=1

    def get_cars(self):
        return [car.get_name()  for car in self.cars ]
        

    def get_carsNum(self):
        return self.cars_num

salon1 = AvtoSalon("GM","Asaka")
salon1.add_cars(avto1)
salon1.add_cars(avto2)
salon1.add_cars(avto3)

# print(salon1.get_cars())
# print(salon1.get_carsNum())

# print(dir(avto1))
# print(avto1.__dict__.keys())

# print(dir(str))
# print(dir(int))
# print(dir(float))
print(dir(bool))