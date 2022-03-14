#REVY RAVLY SABBATHINO SAHETAPY
#5210411227

#Hierarchical Inheritance

#Parent Class
class Induk :
    def fungsiinduk(self) :#5210411227_REVY
        print("Fungsi pada parent class.")

#Class turunan 1
class Anak1(Induk) :
    def fungsianak1(self) :
        print("Fungsi pada anak 1.")

#Class turunan 2
class Anak2(Induk) :
    def fungsianak2(self) :#5210411227_REVY
        print("Fungsi pada anak 2.")

#Objek
child1 = Anak1()
child2 = Anak2()
#5210411227_REVY
child1.fungsiinduk()
child1.fungsianak1()
#5210411227_REVY
child2.fungsiinduk()
child2.fungsianak2()
#5210411227_REVY