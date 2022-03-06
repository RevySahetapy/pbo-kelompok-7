#REVY RAVLY SABBATHINO SAHETAPY
#5210411227
class Menu :
    def __init__(self, nama, deskripsi, harga, stok) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga      #5210411227_REVY
        self.__stok = stok

    def Tampil(self) :
        print(f"{self.nama} harga Rp {self.harga} \n---> {self.deskripsi} sisa stok {self.__stok}\n")

minuman1 = Menu("Jus Sirsak", "Jus Sirsak tanpa gula", 9500, 10)
minuman2 = Menu("Jus Melon", "Jus Melon dengan gula ", 15000, 5)
minuman3 = Menu("Jus Wortel", "Jus Wortel tanpa gula", 15000, 4)
minuman4 = Menu("Coklat", "Smoothie Coklat", 17500, 7)

makanan1 = Menu("Magelangan", "Magelangan dengan telur", 12000, 9)
makanan2 = Menu("Kerak Telor", "Kerak Telor", 15000, 9)
makanan3 = Menu("Kepiting", "Kepiting asem manis", 65000, 11)
makanan4 = Menu("Ikan Bakar", "Ikan Bakar dengan Lalapan", 15000, 5)

pilihan_makanan = [makanan1, makanan2, makanan3, makanan4]
pilihan_minuman = [minuman1, minuman2, minuman3, minuman4]  #5210411227_REVY

print("\nDaftar Menu Makanan\n==========================")
for mkn in pilihan_makanan :
    mkn.Tampil()
print("\nDaftar Menu Minuman\n==========================")
for mn in pilihan_minuman :         #5210411227_REVY
    mn.Tampil()
print("\n")