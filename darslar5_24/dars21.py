def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: >>> ")
        baholar[ism]=int(baho)
    return baholar
talabalar = ["ali","vali","hasan","husan"]
baholar = bahola(talabalar[:])
print(baholar)

# def katta_harf(ismlar):
#     ismlar2 = []
#     while ismlar:
#         ism = ismlar.pop()
#         ism = ism.title()
#         ismlar2.append(ism)
#     return ismlar2    

# ismlar= ["ali","vali","hasan","husan"]
# katta = katta_harf(ismlar[:])
# print(katta)
# print(ismlar)




# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: >>> ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar = ["ali","vali","hasan","husan"]
# baholar = bahola(talabalar[:])
# print(baholar)

