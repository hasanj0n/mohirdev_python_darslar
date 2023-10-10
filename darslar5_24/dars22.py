def summa(x,y,*sonlar):
    """Kiritilgan sonlarning yig'indisini hisoblaydi."""
    yigindi =0
    for son in sonlar:
        yigindi +=son
    return x+y+yigindi    
print(summa(1,2))        
print(summa(1,2,3,4,5))        
print(summa(1,2,4,5,6,7)) 
print(summa(1,2)) 

# def avto_info(kompaniya,model,**malumotlar):
#     """Avtolar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya!"""
#     malumotlar["kompaniya"]=kompaniya
#     malumotlar["model"]=model
#     return malumotlar

# avto1 = avto_info("GM","malibu",rang="qora",yil =2018)
# avto2 = avto_info("KIA","k5",rang="qizil",narh=35000,yil =2018)
# print(avto1)
# print(avto2)



# def kopaytma(*sonlar):
#     kopaytma =1
#     for son in sonlar:
#         kopaytma*= son
#     return kopaytma    
# print(kopaytma(3,7,1,2))
# print(kopaytma(6,7,4,8))
# print(kopaytma(6,5,2,0))

# def talaba_info(ism,familiya,**malumotlar):
#     malumotlar["ism"]=ism
#     malumotlar["familiya"]=familiya
#     return malumotlar
# talaba1 = talaba_info("Hasanjon","Omonov",yoshi =19,kursi =1)
# talaba2 = talaba_info("Sarvar","Omonov",yoshi =20,kursi =2,baho =5)
# print(talaba1)
# print(talaba2)
