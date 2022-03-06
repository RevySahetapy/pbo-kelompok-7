#REVY RAVLY SABBATHINO SAHETAPY
#5210411227
class Buku :
    def __init__(self, judul, pengarang, tahun_terbit, jmlh_halaman) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit        #5210411227_REVY
        self.__jmlh_halaman = jmlh_halaman

    def Tampil(self) :
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah halamannya adalah {self.__jmlh_halaman}\n")

buku1 = Buku("Lebih Senyap", "Andina Dwifatma", 2021, 292)
buku2 = Buku("Dikta & Hukum", "Dhia'an Farah", 2021, 246)
buku3 = Buku("Perempuan Yang Menangis Kepada Bulan Hitam", "Dian Purnomo", 2021, 194)

kumpulan_buku = [buku1, buku2, buku3]
print("\n\tList Buku\n================================")
for buku in kumpulan_buku :     #5210411227_REVY
     buku.Tampil()
print("\n")