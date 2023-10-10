# file = open('sariqdev/dars33/pi.txt')
# PI = file.read()
# print(PI)
# file.close() 





# with open('sariqdev/dars33/pi.txt') as file:
#     pi =file.read()

# pi=  pi.rsplit()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)    



# filename = "sariqdev/dars33/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)



# filename = "sariqdev/dars33/talabalar.txt"
# with open(filename) as file:
#     talabalar = file.readlines()
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)
# print(len(talabalar))

# filename ="new_file.txt"
# ism = "Hasanjon Omonov"
# birthyear =2003
# with open(filename,"w") as file:
#     file.write(ism)
#     file.write(str(birthyear))  


# filename ="new_file.txt"
# ism = "Hasanjon Omonov"
# birthyear =2003
# with open(filename,"w") as file:
#     file.write(ism +"\n")
#     file.write(str(birthyear) + "\n")  

# filename ="new_file.txt"
# ism = "Hasanjon Omonov"
# birthyear =2003
# with open(filename,"a") as file:
#     file.write(ism)
#     file.write(str(birthyear))

import pickle 
talaba1 = {"ism":"Hasanjon","familiya":"Omonov","birtyear":2003,"kurs":2}
talaba2 = {"ism":"Jasur","familiya":"Ergashev","birtyear":2004,"kurs":1}

with open("info","wb") as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

import pickle

with open("info","rb") as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)    
print(talaba1)    
