#REVY RAVLY SABBATHINO SAHETAPY
#5210411227

#Polymorphism dengan Fungsi
print(len("polymorphism"))
print(len([0, 1, 2]))

class jerman :
    def ibukota(self) :
        print("Berlin adalah ibukota negara Jerman")
#5210411227_REVY
class jepang :
    def ibukota(self) :
        print("Tokyo adalah ibukota negara Jepang")

negara1 = jerman()#5210411227_REVY
negara2 = jepang()

for country in (negara1, negara2) :
    country.ibukota()#5210411227_REVY