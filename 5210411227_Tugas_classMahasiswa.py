class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga      #5210411203_Febriyan

minuman1 = Menu("Jus Sirsak", "Jus Sirsak tanpa gula", 10000)
minuman2 = Menu("Jus Melon", "Jus Melon dengan gula ", 17000)
minuman3 = Menu("Jus Wortel", "Jus Wortel tanpa gula", 12000)
minuman4 = Menu("Coklat", "Smoothie Coklat", 18000)

makanan1 = Menu("Kerak Telor", "Kerak Telor", 10000)
makanan2 = Menu("Kepiting", "Kepiting asem manis", 65000)
makanan3 = Menu("Nasi Magelang", "Nasi Magelang dengan Telur", 15000)
makanan4 = Menu("Ikan Bakar", "Ikan Bakar dengan Lalapan", 15000)

pilihan_makanan = [makanan1, makanan2, makanan3, makanan4]
pilihan_minuman = [minuman1, minuman2, minuman3, minuman4]  #5210411203_Febriyan

print("\nDaftar Menu Makanan\n==========================")
for mkn in pilihan_makanan :
    t = '{} harga Rp {}, {}'. format(mkn.nama, mkn.harga, mkn.deskripsi)
    print(t)
print("\nDaftar Menu Minuman\n==========================")
for mn in pilihan_minuman :         #5210411203_Febriyan
    teks = '{} harga Rp {}, {}'. format(mn.nama, mn.harga, mn.deskripsi)
    print(teks)
print("\n")