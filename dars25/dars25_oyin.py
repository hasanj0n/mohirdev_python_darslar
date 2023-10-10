"""SON TOPISH O'YINI"""


from random import randrange



def son_top(x=10):
    print("\nKeling o'ylangan sonni topish o'ynaymiz!")
    kiritilganSon = int(input(f"1 dan {x} gacha son o'yladim.Topa olasizmi?:\n>>>"))
    oylanganSon = randrange(1,x)
    taxminlar = 0
    while True:
        taxminlar +=1
        if kiritilganSon < oylanganSon:
            print("Xato, men o'ylagan son bundan kattaroq,Yana harakat qiling:")
            kiritilganSon = int(input(">>>"))
        elif kiritilganSon > oylanganSon:
            print("Xato, men o'ylagan son bundan kichikroq,Yana harakat qiling:")
            kiritilganSon = int(input(">>>"))
        elif kiritilganSon == oylanganSon:
            print(f"TOPDINGIZ! {oylanganSon} sonini o'ylagan edim.{taxminlar} ta taxmin bilan topdingiz. Tabriklayman!! ") 
            break 
    return taxminlar      

def son_top_pc(x=10):
    input(f"1dan {x} gacha son o'ylang va istalgan sonni yozing. Men topaman. ")
    min = 1
    max = x
    taxminlar  =0
    while True:
        taxminlar +=1
        if min != max:
            taxmin = randrange(min,max)
        else:
            taxmin =min
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t), "
                      f"men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)".lower())
        if javob =="-":
            max = taxmin -1              
        elif javob =="+":
            min = taxmin +1 
        elif javob == "t":
            print(f"Men {taxminlar} ta taxmin bilan topdim!")
            break
    return taxminlar    
                     
def kim_yutdi():
    again  = True
    while again:
        a= son_top()
        b = son_top_pc()
        if a>b:
            print(f"Afsuski, men {a-b} ta taxmin farqi bilan  yutdim!")   
        elif a<b:
            print(f"Tabriklayman, siz {b-a} ta taxmin farqi bilan  yutdingiz!")
        else:
            print(f"Durrang. Ikkalamiz ham {a} ta taxmin bilan topdik!")
        question = input("Yana o'ynaymizmi! (HA yoki YO'Q):\n>>>").upper()
        if question == "HA":
            again = True    
        if question == "YO'Q":
            again = False    




 













