# car0 = {
#     "model":"lacetti",
#     "rang":"oq",
#     "yil":2018,
#     "narh":13000,
#     "km":5000,
#     "divigateli":"avtomat"
# }

# car1 = {
#     "model":"nexia 3",
#     "rang":"qora",
#     "yil":2015,
#     "narh":9000,
#     "km":8900,
#     "divigateli":"mexanika"
# }

# car2 = {
#     "model":"gentra",
#     "rang":"qizil",
#     "yil":2019,
#     "narh":15000,
#     "km":20000,
#     "divigateli":"mexanika"
# }

# car = car2
# print(f"{car ['model'].title()  },"
#     f"{car['rang']} rang , "
#     f"{car['yil']}-yil , {car['narh']}$")

# cars = [car0,car1,car2]
# for car in cars :
#     print(f"{car ['model'].title()  },"
#     f"{car['rang']} rang , "
#     f"{car['yil']}-yil , {car['narh']}$")

# print(f"{cars[1] ['rang'].title()} "
#       f"{cars[1]['model']}"  )

# malibus = []
# for n in range(10):
#     new_car = {
#     "model":"Malibu",
#     "rang":"None",
#     "yil":2022,
#     "narh":None,
#     "km":0,
#     "divigateli":"avto"
#     }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang'] = "qizil"

# for malibu in malibus[3:6]:
#     malibu['rang'] = "qora"

# for malibu in malibus[6:]:
#     malibu['rang'] = "qora"
#     malibu['divigateli'] = "mexanika"

# for malibu in malibus :
#     if malibu["divigateli"]=="avto":
#         malibu["narx"]= 40000
#     else :
#         malibu["narh"] = 35000        

# print(malibus)


# dasturchilar = {
#     "ali" : ["python","c++"],
#     "vali" : ["html","css","js"],
#     "hasan" : ["php","sql"],
#     "ali" : ["python","php"],
#     "ali" : ["c#","c++"]
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# dasturchilar = {
#     "ali" : ["python","c++"],
#     "vali" : ["html","css","js"],
#     "hasan" : ["php","sql"],
#     "ali" : ["python","php"],
#     "ali" : ["c#","c++"]
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper(), end=" ")        
        

# dasturchilar = {
#     "ali" : {"familiya":"valiyev",
#              "tyili":1995,
#              "malumot":"oliy",
#              "tillar":["python","c++"]},
#     "vali" : {"familiya":"aliyev",
#              "tyili":2001,
#              "malumot":"o'rta-maxsus",
#              "tillar":["html","css","js"]},
#     "ali" : {"familiya":"omonov",
#              "tyili":2003,
#              "malumot":"oliy",
#              "tillar":["python","js","html"]}
# }
# for ism , info in dasturchilar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyili']}-yilda tug'ulgan. "
#           f"Malumoti:{info['malumot']}. \n "
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info["tillar"]:
#         print(til.upper())







####################################################################################################################################################################################################


# mashhur1 ={
#     "ismi":"Navoiy",
#     "sohasi":"adabiyot",
#     "tjoyi":"hirot",
#     "tyili":1401,
#     "yaratgan":["xamsa","mahbub ul-qulub","qush tili"]
# }
# mashhur2 ={
#     "ismi":"Xorazmiy",
#     "sohasi":"ilm-fan",
#     "tjoyi":"xorazm",
#     "tyili":780,
#     "yaratgan":["al-jabr","val-muqobala","geometry"]
# }
# mashhur3 ={
#     "ismi":"Mozart",
#     "sohasi":"musiqa",
#     "tjoyi":"austria",
#     "tyili":1756,
#     "yaratgan":["skripka","piano","fleyta"]
# }
# mashhur4 ={
#     "ismi":"DaVinci",
#     "sohasi":"sa'nat",
#     "tjoyi":"italy",
#     "tyili":1452,
#     "yaratgan":["mona lisa","salvator mundi","the last supper"]
# }
# mashhurlar = [mashhur1,mashhur2,mashhur3,mashhur4]

# for mashhur_shaxs in mashhurlar:
#     print(f"{mashhur_shaxs['ismi'].title()} {mashhur_shaxs['tyili']}-yilda {mashhur_shaxs['tjoyi'].title()}da tug'ulgan."
#           f" U  {mashhur_shaxs['sohasi']} sohasida ish yuritgan. \n"
#           "Yaratgan asarlari:")
#     for asarlar in mashhur_shaxs['yaratgan']:
#         print(asarlar.upper()) 


# kinolar = {
#     "otam": ["shaytanat", "inception", "tenet"],
#     "akam": ["teminator", "rembo", "john wick"],
#     "onam": ["titanic", "abdullajon", "mahalladda duv duv gap"],
# }
# for oila_azosi, films in kinolar.items():
#     print(f"{oila_azosi.capitalize()}ning sevimli filmlari: ")
#     for film in films :
#         print(film.upper()) 








# davlatlar = {
#     "country1" : {
#         "name":"uzbekistan",
#         "capital":"tashkent",
#         "area":447_000,
#         "population":34_230_000,
#         "currency":"so'm",
#     },
#     "country2" : {
#         "name":"russia",
#         "capital":"moscow",
#         "area":17_100_000,
#         "population":144_100_000,
#         "currency":"rubl",
#     },
#     "country3" : {
#         "name":"usa",
#         "capital":"washington",
#         "area":9_834_000,
#         "population":329_500_000,
#         "currency":"dollar",
#     },
#     "country4" : {
#         "name":"france",
#         "capital":"paris",
#         "area":543_940,
#         "population":67_390_000,
#         "currency":"euro",
#     },
#     "country5" : {
#         "name":"malasia",
#         "capital":"Kuala Lumpur",
#         "area":329_847,
#         "population":106_435_000,
#         "currency":"ringgit",
#     }
# }

# for country, info in davlatlar.items():
#     print(f"{info['name'].capitalize()}ning poytaxti {info['capital'].capitalize()}.\n"
#           f"Hududi:{info['area']}km \n"
#           f"Aholisi:{info['population']} kishi\n"
#           f"Pul birligi:{info['currency']} \n\n"
# )


davlatlar = {
    "uzbekistan" : {
        "capital":"tashkent",
        "area":447_000,
        "population":34_230_000,
        "currency":"so'm",
    },
    "russia" : {
        "capital":"moscow",
        "area":17_100_000,
        "population":144_100_000,
        "currency":"rubl",
    },
    "usa" : {
        "capital":"washington",
        "area":9_834_000,
        "population":329_500_000,
        "currency":"dollar",
    },
    "france" : {
        "capital":"paris",
        "area":543_940,
        "population":67_390_000,
        "currency":"euro",
    },
    "malasia" : {
        "capital":"Kuala Lumpur",
        "area":329_847,
        "population":106_435_000,
        "currency":"ringgit",
    }
}

a =input("Davlat nomini kiriting:").lower()

if a in davlatlar.keys():
    info =davlatlar[a]
    print(f"\n{a.capitalize()}ning poytaxti {info['capital'].capitalize()}.\n"
        f"Hududi:{info['area']}km^2 \n"
        f"Aholisi:{info['population']} kishi\n"
        f"Pul birligi:{info['currency']}\n")
else :
    print("Lug'atda bunday davlat yo'q")






        