talaba_0 = {
    "ism":"hasanjon",
    "familiyasi":"omonov",
    "yosh":"18",
    "t_yil":"2003"
    }

# print(talaba_0.items())
for key , value in talaba_0.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value} \n")

# telefonlar = {
#     "ali":"iphone X",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310",
#     "anvar":"3xl"
#     }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni bu {q}. ")   



# mahsulotlar ={
#     "olma":10000,
#     "tarvuz":8000,
#     "qovun":11000,
#     "anor":20000,
#     "shaftoli":25000,
#     "uzum":40000
#     }

# print("do'kondagi mahsulotlar:")
# for a in mahsulotlar.keys():
#     print(a.title())    


# bozorlik =["anor", "uzum", "tuxum","tuz"]
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for mahsulot in mahsulotlar:
#     if mahsulot not in bozorlik:
#         print(f"Iltimos, do'koningizda {mahsulot} ham olib keling!")

# print("Do'kondagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


# print(telefonlar.values())

# print("Foydalanuvhchilar quyidagi telefonlarni ishlatadilar:")
# for tel in  telefonlar.values():
#     print(tel.title())


# telefonlar = {
#     "ali":"iphone X",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310",
#     "anvar":"3xl",
#     "anvar":"galaxy s9",
#     "anvar":"mi 10 pro",
#     "anvar":"iphone X",
#     "anvar":"iphone X"
#     }
# print("Foydalanuvhchilar quyidagi telefonlarni ishlatadilar:")
# for tel in  set(telefonlar.values()):
#     print(tel.title()) 

# toys ={"ball","car","lamp","ball","bear","car"}
# print(toys)





####################################################################################################################################################################################################


# py_lugat= {
#     "Integer":"Butun son",
#     "Boolean":"Mantiqiy qiymat",
#     "Float":"O'nlik son",
#     "If":"shartlarni tekshirish operatori",
#     "For":"Takrorlash operatori",
#     "Print":"cnsolega chiqarish",
#     "Sin":"sinus formulasi",
#     "Cos":"cosinus formulasi",
#     "While":"Takrorlash operatori2",
#     "Abs":"Sonning absalyut qiymati"
#     }
# for key , value in sorted(py_lugat.items()) :
#     print(f"{key} - {value} ") 

# davlatlar= {
#     "Rossiya":"Moskva",
#     "Italiya":"Rim",
#     "Ispaniya":"Madrid",
#     "Aqsh":"Washington",
#     "Fransiya":"Paris",
#     "Xitoy":"Pekin",
#     "Janubiy Koreya":"Seoul",
#     "O'zbekiston":"Tashkent",
# }
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat)

# print("Dunyo davlatlarining poytaxtlari:")
# for capital in sorted(davlatlar.values()):
#     print(capital)

# davlat = input("Davlat nomini kiriting:")
# capital = davlatlar.get(davlat)
# if davlat == None:
#     print(f"Kecharisiz bizda bunday davlat yo'q! ")
# else:
#     print(f"{davlat.upper()}ning poytaxti {capital.title()} ")


# mevalar ={
#     "olma":10000,
#     "tarvuz":8000,
#     "qovun":11000,
#     "anor":20000,
#     "shaftoli":25000,
#     "uzum":40000,
#     "nok":6300,
#     "behi":4100
# }
# bozorlik = []
# a,b,c = input("Uch xil meva turini kiriting: \n>>>").split()
# bozorlik.append(a)
# bozorlik.append(b)
# bozorlik.append(c)

# for meva in bozorlik :
#     if meva in mevalar:
#         print(f"{ meva.title() } {mevalar[meva]} so'm  ")
# for meva in bozorlik :
#     if meva not in mevalar:
#         print(f"Bizda {meva} yo'q")






