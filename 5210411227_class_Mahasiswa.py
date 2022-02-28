class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


m1 = Mahasiswa("Budiman", "10120209", "Teknik Komputer", 2019)

teks = '{} adalah mahasiswa {} dengan nim {}'.format(m1.nama, m1.prodi, m1.nim)
print(teks)
