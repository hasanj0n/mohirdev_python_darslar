# mevalar =['olma','anjir','shaftoli','o\'rik']
# narxlar =[1000,1300,4120,4667,2354]
# sonlar =["bir", "ikki", 3,4,5]
# ism =[]
# mevalar[0]="anor"
# print(mevalar[0].title())
# print(narxlar[1]+narxlar[2])

# mevalar.append("gilos")
# mevalar.append("uzum")
# mevalar.insert(1,"uzum")
# print(mevalar)

# cars =["cobalt", "nexia", "malibu"]
# cars.append("tracker")
# del  cars[0]
# cars.insert(0,"matiz")
# cars.remove("matiz")

# mashina = cars.pop(-1)
# print(cars)

# names = ["Istam","Barkamol","Shuhrat","Tolib","Husniddin"]
# print(f"Salom {names[0]}!")
# print(f"Ielts darsga borayapsanmi {names[1]}?")
# print(f"{names[2]},Toshkentga keldingmi?")
# print(f"{names[3]},Toshkentga keldingmi?")
# print(f"{names[-1]},Toshkentga keldingmi?")

# numbers =[1986, -367, 65.7, 576, 184, 0, -237]
# a = numbers[0]-numbers[1]
# b = numbers[2]*5
# numbers.append(2000)
# numbers.insert(1,1.5)
# numbers[4]=18
# print(a,b)
# print(numbers)

# t_shaxslar = ["Amir Temur","Alisher Navoiy","Mirzo Ulug'bek","Ibn Sino"]
# z_shaxslar = ["Bill Gates","Ilon Mask","Jack Maa"]
# a= t_shaxslar.pop(2)
# b= z_shaxslar.pop(-1)
# print(f"Men tarixiy shaxslardan {a} bilan, zamonaviy shaxslardan esa {b} bilan suhbat qilmoqchiman!")

# friends =[ ]
# friends.append("Jasur")
# friends.append("Jamshid")
# friends.append("Shuhrat")
# friends.append("Istam")
# friends.append("Tolib")
# friends.remove("Jamshid")
# friends.insert(0,"Alisher")
# friends.insert(-1,"Aslbek")
# friends.insert(2,"Asliddin")
# a=friends.pop(0)
# b=friends.pop(0)
# c=friends.pop(0)
# d=friends.pop(0)
# e=friends.pop(0)
# h=friends.pop(0)
# g=friends.pop(0)
#
# guests = []
# guests.append(a)
# guests.append(b)
# guests.append(c)
# guests.append(d)
# guests.append(e)
# guests.append(h)
# guests.append(g)
#
#
# print(friends)
# print(guests)

# numbers1 = list(range(0, 12, 2))
# numbers1 = sorted(numbers1, reverse=True)
numbers2 = [4, 2, 14, 23, 54, 17, 72]
# print(sorted(numbers2, reverse=True))
# print(numbers1)
print(max(numbers2))
print(min(numbers2))
numbers3 = numbers2[:]  # listdan nusxa olish
print(numbers3)
# print(sum(numbers1))
# print(numbers1+numbers2)

cars = ["cobalt", "tracker", "matiz", "spark", "malibu"]
# cars.sort()
# print(cars)
cars_tuple = tuple(cars)
# cars_tuple[0] = "nexia"  # tuple elemnetlarini o'zgartirib bo'lmaydi
print(cars_tuple)

numbers120 = list(range(120, 1202, 2))
print(sum(numbers120))
print(max(numbers120) - min(numbers120))
print(len(numbers120))
