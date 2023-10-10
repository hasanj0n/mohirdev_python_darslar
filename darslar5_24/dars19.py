# def salom_ber(ism,familiya):
#     ''' Foydalanuvchidan ismini qabul qilib, salom beruvchi funksiya'''
#     print(f"Assalomu alekum,{familiya} {ism.title()}! ")
# salom_ber("Hasanjon","Omonov")

# def yoshni_hisobla(ism,tugulgan_yil,joriy_yil=2022):
#     '''Tug'ulgan yilni hisoblovchi funksiya'''
#     print(f"{ism.title()}, siz {joriy_yil-tugulgan_yil} yoshdasiz. ")
# yoshni_hisobla("Hasanjon",2003)

##############################################################################################################################################################################################################################################################################################################################################################################

# def tugulganYilni_hisobla(ism,yoshingiz,joriy_yil=2022):
#     '''Tug'ulgan yilni hisoblovchi funksiya'''
#     print(f"{ism.title()}, siz {joriy_yil-yoshingiz} yilda tug'ulgansiz. ")
# tugulganYilni_hisobla("Hasanjon",19)


# def kva_kub(x):
#     '''Berilgan x ni kvadrati va kubini hisoblovchi funksiya'''
#     print(f"x sonning kvadrati:{x**2},kubi:{x**3} ")
# kva_kub(6) 


# def juft_toq(x):
#     '''Berilgan x ni juft yoki toqligini aniqlovchi funksiya'''
#     if x%2==0:
#         print(f"Berilgan x juft son.")
#     else:
#         print("Berilgan x toq son.")    
# juft_toq(4) 

# def katta_kichik(x,y):
#     '''Berilgan x, y larni kattasini aniqlovchi funksiya.'''
#     if x>y:
#         print(f"Katta son:x={x} ")
#     if x<y:
#         print(f"Katta son:y={y} ")
#     else:
#         print("Sonlar teng!")    
# katta_kichik(5,5) 

# def katta_kichik(x,y):
#     '''Berilgan x ni y-darajasini aniqlovchi funksiya.'''
#     print(f"{x}ni {y}-darajasi:{x**y} ")
# katta_kichik(5,4) 

def bolinish_belgilari(x):
    '''Berilgan sonni 2-10 oraliqda qoldiqsiz bo\'linadiganlarini topuvchi funksiya.'''
    for n in range(2, 11):
        if x % n == 0:
            print(f"{x} {n}ga qoldiqsiz bo'linadi.")


bolinish_belgilari(70)
