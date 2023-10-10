


class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya

    def get_age(self,yil=2022):
        return yil-self.tyil    


    def tanishtir(self):
         return (f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil} yil. ")


talaba1 = Talaba("Hasanjon","Omonov",2003)
talaba2 = Talaba("Istam","Nazirov",2004)

print(talaba1.tanishtir())
print(talaba2.tanishtir())
print(talaba1.get_name())
print(talaba1.get_lastname())
print(talaba1.get_age())

class User :
    def __init__(self,name,surname,username,email,phonenumber):
        self.name = name
        self.sname = surname
        self.uname = username
        self.mail = email
        self.number = phonenumber

    def get_info(self):
        return (f"Foydalanuvchi: {self.uname}, to'liq ismi: {self.name} {self.sname}, emaili: {self.mail}, telefon raqami: {self.number}. ")
    def get_surname(self):
        return self.sname
    def get_telcom(self):
        pass

user1 = User("Hasanjon","Omonov","h@sanjon","omonovhasan001@gmail.com",+998940021011)  

print(user1.get_info())
print(user1.get_surname())
print(user1.get_telcom())