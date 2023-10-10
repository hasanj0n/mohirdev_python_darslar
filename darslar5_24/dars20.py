# def toliq_ism_yasa(ism,familiya):
#     '''To'liq ism qaytaruvchi funksiya'''
#     toliq_ism = f"{ism} {familiya} "
#     return toliq_ism

# a1=toliq_ism_yasa("Hasanjon","Omonov")
# a2=toliq_ism_yasa("Jasur","Ergashev")
# print(f"Darsga kelmagan talabalar:{a1},{a2}")






# def toliq_ism_yasa(ism,familiya,otasining_ismi=""):
#     '''To'liq ism qaytaruvchi funksiya'''
#     if otasining_ismi:
#         toliq_ism= f"{ism} {otasining_ismi} {familiya} "
#     else:
#         toliq_ism =f"{ism} {familiya} "    
#     return toliq_ism.title() 

# a1=toliq_ism_yasa("Hasanjon","Omonov","Nuralivich")
# a2=toliq_ism_yasa("Jasur","Ergashev")
# print(f"Darsga kelmagan talabalar:{a1},{a2}")






# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {
#         "kompaniya":kompaniya,
#         "model":model,
#         "rang":rangi,
#         "korobka":korobka,
#         "yil":yili,
#         "narh":narhi
#     }
#     return avto

# avto1 =avto_info("GM","Malibu","Qora","Avtomat",2018)
# avto2 =avto_info("GM","Gentra","Oq","Mexanika",2020,15000)
# avtolar =[avto1,avto2]
# print("Online bozorda mavjud mashinalar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narxi:{narh} ")    


# def oraliq(min,max):
#     '''oddiy range funksiyasiga o'xshagan funksiya.'''
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=1
#     return sonlar 

# print(oraliq(0,10))
# print(list(range(0,10)))

# def oraliq(min,max,step=1):
#     '''qadamli range funksiyasiga o'xshagan funksiya.'''
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=int(step)
#     return sonlar 

# print(oraliq(0,30,2))
# print(list(range(0,30,2)))


def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto = {
        "kompaniya":kompaniya,
        "model":model,
        "rang":rangi,
        "korobka":korobka,
        "yil":yili,
        "narh":narhi
    }
    return avto

print("Saytimizda avtolar ro'yhatini shakllantiramiz.")
avtolar =[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting:",end=" ")
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")
    avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
    javob = input("Yana avto qo'shasizmi?(yes/no): ")
    if javob == "no":
        break

print("Online bozorda mavjud mashinalar:")
for avto in avtolar:
    if avto["narh"]:
        narh = avto["narh"]
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narxi:{narh} ")

##############################################################################################################################################################################################################################################################################################################################################################





# def toliq_malumot(ism,familiyasi,tugilgan_yili,tugulgan_joyi,email=None,phoneNumber=None):
#     malumot ={
#     "Ism":ism,
#     "Familiya":familiyasi,
#     "tugulgan_joyi":tugulgan_joyi,
#     "tugilgan_yili":tugilgan_yili,
#     "yoshi":2022-tugilgan_yili,
#     "email":email,
#     "phoneNumber":phoneNumber
#     }
#     return malumot

# mijozlar =[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:",end=" ")
#     ism = input("Ismingiz: ")
#     familiyasi = input("Familiyangiz: ")
#     tugulgan_joyi = input("Tug'ilgan joyiingiz: ")
#     tugilgan_yili = input("Tug'ilgan yilingiz: ")
#     email = input(":Emalingiz(Majburiy emas!): ")
#     phoneNumber = input(":Telefon raqamingiz(Majburiy emas!): ")
#     mijozlar.append(toliq_malumot(ism,familiyasi,tugulgan_joyi,tugilgan_yili,email,phoneNumber))
#     javob = input("Yana malumot qo'shasizmi?(yes/no): ")
#     if javob == "no":
#         break

# talaba1 = toliq_malumot("Hasanjon","Omonov",2003,"Qashqadaryo","",+998915609650)
# print(talaba1)






# def kattaRaqamni_chiqar(a,b,c):
#     if a>=b and a>=c:
#         x=a
#     elif b>=a and b>=c:
#         x =b
#     else:
#         x=c
#     return x            
# katta_son=kattaRaqamni_chiqar(8,8,7)
# print(katta_son)





# from cmath import pi
# def circle(r):
#     aylana = {
#         "radius":r,
#         "diametr":2*r,
#         "perimetr":2*r*pi,
#         "yuz":pi*r**2
#     }
#     return aylana
# aylana1 = circle(6)
# print(f"Aylana radiusi:{aylana1['radius']},  Aylana diamtri:{aylana1['diametr']}, Aylana perimetri:{aylana1['perimetr']},  Aylana yuz:{aylana1['yuz']}")

# tubsonlar =[]
# def tubSonlar(min,max):    
#     for n in range(min,max+1):
#         Tub =True
#         if n==1:
#             Tub =False
#         elif n==2:
#             Tub = True
#         else:
#             for x in range(2,n):
#                 if n%x ==0:
#                     Tub =False
#         if Tub:
#             tubsonlar.append(n) 
#         return tubsonlar                       
        
# a=tubSonlar(5,18)
# print(a)

# min = 1
# max = 100
# tubsonlar =[]
# for n in range(min,max+1):
#     tub = True
#     if n== 1:
#         tub = False
#     elif n==2:
#         tub = True
#     else:
#         for x in range(2,n):
#             if n%x==0:
#                 tub = False
#     if tub :
#         tubsonlar.append(n)            
# print(tubsonlar)


# fibonachchi_sonlari =[]

# n = 20
# for x in range(n):
#     if x==0 or x==1:
#         fibonachchi_sonlari.append(1)
#     else:
#         fibonachchi_sonlari.append(fibonachchi_sonlari[x-1]+fibonachchi_sonlari[x-2])
# print(fibonachchi_sonlari)







