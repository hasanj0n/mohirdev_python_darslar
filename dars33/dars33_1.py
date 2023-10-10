

# with open("sariqdev/dars33/ok.txt") as file:
#     text = file.read()
# print(text) 


# import pickle


# with open("sariqdev/dars33/pi_million_digits.txt") as file:
#     pi = file.read()
# pi = pi.rstrip() 
# pi = pi.replace("\n","")
# pi = pi.replace(" ","")
# # bdate = input("Tug'ilgan sanangizni kiriting(10112003):")
# # print(bdate in pi)


# pi =float(pi)

# with open("pi_float.dat","wb") as file:
#     pickle.dump(pi,file)


while True:
    book = input("Yaxshi ko'rgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('sariqdev/dars33/books.txt','a') as file:
        file.write(book+'\n')