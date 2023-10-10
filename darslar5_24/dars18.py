# print("Yaqin do'stlaringiz ro'yhatini tuzing")
# ismlar=[]
# n=1
# while True:
#     savol = f"{n}-do'tingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash= input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != "ha":
#         break
# print("Do'stlaringiz ro'yhati:")
# for dost in ismlar:
#     print(dost.title())  








# dostlar ={}
# ishora = True

# while ishora:
#     ism = input("Do'tingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)

#     javob = input("Yana ma'lumot qo'shasizmi (ha/yo'q)")
#     if javob == "yo'q" :
#         ishora=False


# for ism ,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh}da. ")    

# cars  = ["lacetti","nexia","toyota","nexia","audi","malibu","nexia","lacetti"]
# car = "lacetti"
# while car in cars:
#     cars.remove(car)
# print(cars)    




# talabalar  = ["hasan","husan","ali","botir","olim"]
# baholangan_talablar ={}

# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talablar[talaba]=int(baho)

# print("\nUmumiy ro'yhat:")
# for ism , baholar in baholangan_talablar.items():
#     print(f"{ism.title()}ning bahosi: {baholar} ")    



#########################################################################################################################################################################################################################################################################################################################################################


# print("Buyurtma bering")

# mahsulotlar = []
# n=1 
# while True:
#     savol = f"{n}-mahsulotni kiriting: "
#     n+=1
#     mahsulot = input(savol)
#     mahsulotlar.append(mahsulot)
#     savol1 = input("Yana mahsulot buyurtma qilasizmi:(ha/yo'q)")
#     if savol1 != "ha":
#         break

# print("\nBuyurtma qilgan mahsulotlaringiz:")
# for mahsulot1 in mahsulotlar:
#     print(mahsulot1)






# savat =  {}
# ishora = True
# while ishora:
#     nomi = input("Mahsulot nomini kiriting:")
#     narxi = input(f"{nomi.title()}ning narxi:")
#     savat[nomi]=int(narxi)
#     savol = input("Yana mahsulot haqida ma'lumot kiritasizmi:(ha/yo'q)")
#     if savol != "ha":
#         ishora = False

# print("Mahsulotlar:")     
# for a,b in savat.items():
#     print(f"{a}ning narxi {b}so'm. ") 


# from operator import length_hint, truediv

# savat = ["olma","uzum","anor","nok","behi","banan","apelsin"]
# mahsulotlar = {"anor":200,"nok":500,"olma":400}


# while True:
#     meva = savat.pop()
#     a= length_hint(savat)
#     if meva in mahsulotlar:
#         print(f"{meva.title()}ning narxi {mahsulotlar[meva]}. ")
#     else:
#         print(f"Bizda {meva} yo'q.")
#     if  a ==0:
#         break   



      







