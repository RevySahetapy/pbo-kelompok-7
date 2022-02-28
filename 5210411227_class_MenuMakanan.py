class MenuMakanan:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga


mknan1 =  MenuMakanan("Kerak Telor", "Kerak Telor", 10000)
mknan2 = MenuMakanan("Kepiting", "Kepiting asem manis", 65000)
mknan3 = MenuMakanan("Nasi Magelang", "Nasi Magelang dengan Telur", 15000)
mknan4 = MenuMakanan("Ikan Bakar", "Ikan Bakar dengan Lalapan", 15000)

pilihan_makanan = [mknan1, mknan2, mknan3, mknan4]
print("Daftar Menu Makanan")
for mn in pilihan_makanan:
    t = '{} harga Rp {}, {}'. format(mn.nama, mn.harga, mn.deskripsi)
    print(t)