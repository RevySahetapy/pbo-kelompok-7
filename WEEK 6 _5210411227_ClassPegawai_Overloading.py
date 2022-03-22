#REVY RAVLY SABBATHINO SAHETAPY
#5210411227

#Implementasi Overloading Class Pegawai
class Pegawai :
    jumlah = 0
#5210411227_REVY
    def __init__(self, nama, gaji) :
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilJumlah(self) :
        print(f"Total Pegawai : {Pegawai.jumlah}")
    #5210411227_REVY
    def tampilPegawai(self) :
        print(f"Nama Pegawai : {self.nama}")

    def tunjangan(self, istri = None, anak = None) :
        if anak != None and istri != None :
            total = anak + istri
            print(f"Tunjangan anak + istri = {total}")
        else :#5210411227_REVY
            total = istri
            print(f"Tunjangan istri = {total}")

pegawai1 = Pegawai("Eren", 2000)
pegawai2 = Pegawai("Luffy", 6000)
#5210411227_REVY
pegawai1.tampilPegawai()
pegawai2.tampilPegawai()

pegawai1.tunjangan(2500, 2000)  #Overloading
pegawai2.tunjangan(2500)        #Overloading
#5210411227_REVY
print("Total pegawai = %d" % Pegawai.jumlah)
rataGaji = (pegawai1.gaji + pegawai2.gaji) / Pegawai.jumlah
print(f"Rata-rata gaji = {str(rataGaji)}")