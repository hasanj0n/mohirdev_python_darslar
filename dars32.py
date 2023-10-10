class Avto:
    """Avtomobil klasi"""
    __num_avto =0
    def __init__(self,make,model,color,year,cost) :
        self.make =make
        self.model =model
        self.color =color
        self.year =year
        self.cost =cost        
        Avto.__num_avto +=1

    # def __str__(self):
    #     return f"Avto:{self.make} {self.model} " 


    def __repr__(self):
        return f"Avto:{self.make} {self.model} "  

    def __eq__(self,y):
        return self.cost == y.cost 

    def __lt__(self,y):
        return self.cost < y.cost 

    def __le__(self,y):
        return self.cost <= y.cost





avto1 = Avto("GM","Cobalt","Qora",2019,150000)
avto2 = Avto("Lada","Vesta","Oq",2020,16000)
avto3 = Avto("Hyundai","Tucson","Qizil",2022,250002)


# print(dir(Avto))
# print(avto1)
# print(avto1==avto2)
# print(avto1<avto2)
# print(avto1>=avto2)

class AvtoSalon:
    """Avtosalon klasi"""
    def __init__(self,name):
        self.name =name
        self.avtolar = []

    def __repr__(self) -> str:
        return f"{self.name} avtosaloni."

    def __getitem__(self,index):
        return self.avtolar[index]    

    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)    
            else:
                print("Avto kiriting.")    

salon1 = AvtoSalon("MaxAvto")            

print(salon1)

avto1 = Avto("GM","Cobalt","Qora",2019,150000)
avto2 = Avto("Lada","Vesta","Oq",2020,16000)
avto3 = Avto("Hyundai","Tucson","Qizil",2022,250002)

salon1.add_avto(avto1,avto2,avto3)

print(salon1[:])