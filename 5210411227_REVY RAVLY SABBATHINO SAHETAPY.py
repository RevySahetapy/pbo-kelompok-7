#REVY RAVLY SABBATHINO SAHETAPY
#5210411227
class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

minuman1 = Menu("Jus Sirsak", "Jus Sirsak tanpa gula", 10000)
minuman2 = Menu("Jus Melon", "Jus Melon dengan gula ", 17000)
minuman3 = Menu("Jus Wortel", "Jus Wortel tanpa gula", 12000)
minuman4 = Menu("Coklat", "Smoothie Coklat", 18000)

makanan1 = Menu("Kerak Telor", "Kerak Telor", 10000)
makanan2 = Menu("Kepiting", "Kepiting asem manis", 65000)
makanan3 = Menu("Nasi Magelang", "Nasi Magelang dengan Telur", 15000)
makanan4 = Menu("Ikan Bakar", "Ikan Bakar dengan Lalapan", 15000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswaE = Mahasiswa("Havin", "5210411016", "Informatika")
mahasiswaF = Mahasiswa("Revy", "5210411019", "Informatika")
mahasiswaG = Mahasiswa("Zidni", "5210411117", "Informatika")
mahasiswaH = Mahasiswa("Hanaya", "5210411213", "Informatika")

mahasiswa = [mahasiswaE, mahasiswaF, mahasiswaG, mahasiswaH]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Lebih Senyap", "Andina Dwifatma", 2021)
buku2 = Buku("Dikta & Hukum", "Dhia'an Farah", 2021)
buku3 = Buku("Perempuan Yang Menangis Kepada Bulan Hitam", "Dian Purnomo", 2021)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")