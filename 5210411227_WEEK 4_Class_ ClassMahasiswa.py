#REVY RAVLY SABBATHINO SAHETAPY
#5210411227
class Mahasiswa :
    def __init__ (self, nama, nim, prodi, universitas) :
        self.nama = nama
        self.nim = nim      #5210411227_REVY
        self.prodi = prodi
        self.__universitas = universitas

    def Tampil(self) :
        print(f"{self.nama} adalah mahasiswa {self.__universitas} prodi {self.prodi} dengan nim {self.nim}")

mahasiswa1 = Mahasiswa("Revy", "5210411227", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa2 = Mahasiswa("Havin", "5210411212", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa3 = Mahasiswa("Febriyan", "5210411203", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa4 = Mahasiswa("Nadia", "5210411245", "Informatika", "Universitas Teknologi Yogyakarta")

kumpulan_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\n\tList Mahasiswa\n================================")
for mhs in kumpulan_mahasiswa :     #5210411227_REVY
    mhs.Tampil()
print("\n")