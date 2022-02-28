class MenuMinuman:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga


mnm1 = MenuMinuman("Jus Jambu", "Jus jambu merah Dengan gula", 1000)
mnm2 = MenuMinuman("Jus Alpukat", "Jus alpukat Tanpa gula", 12000)
mnm3 = MenuMinuman("Jus Mangga","Jus Mangga dengan campuran gula", 15000)
mnm4 = MenuMinuman("Americano", "Americano Dengan Gula", 21000)

pilihan_minuman = [mnm1, mnm2, mnm3, mnm4]
print("Daftar Menu Healty Fruits")
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}'. format(mn.nama, mn.harga, mn.deskripsi)
    print(t)
