#NAMA : REVY RAVLY SABBATHINO SAHETAPY
#NIM : 5210411227

class Perpustakaan :
    def __init__(self, kode, judul, subjek, lokasi, info) :
        self.kode = kode
        self.judul = judul      #5210411227_REVY RAVLY SABBATHINO SAHETAPY
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal        #5210411227_REVY RAVLY SABBATHINO SAHETAPY
        self.ukuran = ukuran      
           

    def Tampil(self) :
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Pengarang : {self.pengarang}")
        print(f"Jumlah Halaman : {self.jmlhal}")
        print(f"Kategori : {self.subjek}\n")

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Volume : {self.volume}")
        print(f"Issue : {self.issue}")
        print(f"Kategori : {self.subjek}\n")
#5210411227_REVY RAVLY SABBATHINO SAHETAPY
class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre      #5210411227_REVY RAVLY SABBATHINO SAHETAPY

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Aktor : {self.aktor}")
        print(f"Genre : {self.genre}")
        print(f"Kategori : {self.subjek}\n") 

#Objek Buku
buku1 = Buku("123", "Pemrograman Python", "Buku Cetak", "Rak 1", "Dipinjam", "945-884-98-05", "Yogi Syarif", 20, "25x15")
buku2 = Buku("134","Perancangan Sistem Kendali", "Buku Ajar", "Rak 1", "Ada", "978-602-453-239-0", "Noor Colis Basjaruddin", 120, "15x23")
buku3 = Buku("156","Collaborative Governance", "Buku Referensi", "Rak 1", "Ada", "978-602-475-963-6", "La Ode Syaiful Islamy", 166, "15x20")
buku4 = Buku("178","Algoritma dan Pemrograman Python", "Buku Referensi", "Rak 1", "Dipinjam", "978-623-02-3810-9", "Ferawaty", 96, "17x25")

#Objek Majalah
majalah1 = Majalah("234", "Dunia Komputer", "Majalah Cetak", "Rak 2", "Ada", "VII", "Komputer")
majalah2 = Majalah("256", "Book Selections", "Majalah Cetak", "Rak 2", "Dipinjam", "IV", "Musik")
majalah3 = Majalah("278", "Naruto Shipudden", "Majalah Manga", "Rak 2", "Ada", "CIX", "Anime")
majalah4 = Majalah("290", "Bleach", "Majalah Manga", "Rak 2", "Ada", "LXXVI", "Anime")  #5210411227_REVY RAVLY SABBATHINO SAHETAPY
majalah5 = Majalah("265", "Itachi Story", "Majalah Manga", "Rak 2", "Dipinjam", "I", "Anime")

#Objek DVD
dvd1 = DVD("312", "Dragon Ball", "softcopy", "Rak 3", "Ada", "Goku", "Anime")
dvd2 = DVD("323", "Jujutsu Kaisen", "softcopy", "Rak 3", "Ada", "Gojo", "Anime")
dvd3 = DVD("334", "Pokemon", "softcopy", "Rak 3", "Ada", "Ash", "Anime")    #5210411227_REVY RAVLY SABBATHINO SAHETAPY
dvd4 = DVD("398", "Naruto", "softcopy", "Rak 3", "Ada", "Naruto", "Anime")

while True :
    print("=======================\n    SEARCH ITEM \n=======================")
    print("1. BUKU ")  #FEBRIYAN BIOPSA MINANDA
    print("2. MAJALAH")
    print("3. DVD")
    print("0. selesai")
    menu = input("Pilihan Menu : ") 

    if menu == '1' :
        print("\nMENU BUKU\n===============\n1. Tampil Buku")
        print("2. Cari Buku")   #5210411227_REVY RAVLY SABBATHINO SAHETAPY
        pilihan = input("Pilihan : ")  
        buku = [buku1, buku2, buku3, buku4]

        if pilihan == '1' :
            print("\n==============================================")
            for buku in buku :
                buku.Tampil()#5210411227_REVY RAVLY SABBATHINO SAHETAPY

        elif pilihan == '2' :
            kode = input("Masukan Kode Buku\t: ")
            for x in buku :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")    #5210411227_REVY RAVLY SABBATHINO SAHETAPY
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '2' :
        print("\nMENU MAJALAH\n===============\n1. Tampil Data Majalah")
        print("2. Cari Majalah")        #5210411227_REVY RAVLY SABBATHINO SAHETAPY
        pilihan = input("Pilihan : ") 
        majalah = [majalah1, majalah2, majalah3, majalah4, majalah5] 

        if pilihan == '1' :
            print("\n==============================================")
            for majalah in majalah :
                majalah.Tampil()#5210411227_REVY RAVLY SABBATHINO SAHETAPY

        elif pilihan == '2' :
            kode = input("Masukan Kode Majalah\t: ")
            for x in majalah :#5210411227_REVY RAVLY SABBATHINO SAHETAPY
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '3' :
        print("\nMENU DVD\n===============\n1. Tampil Data DVD")
        print("2. Cari DVD")
        pilihan = input("Pilihan : ")  
        dvd = [dvd1, dvd2, dvd3, dvd4]  #5210411227_REVY RAVLY SABBATHINO SAHETAPY

        if pilihan == '1' :
            print("\n==============================================")
            for dvd in dvd :
                dvd.Tampil()#5210411227_REVY RAVLY SABBATHINO SAHETAPY

        elif pilihan == '2' :
            kode = input("Masukan Kode DVD\t: ")
            for x in dvd :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")
#5210411227_REVY RAVLY SABBATHINO SAHETAPY
    elif menu == '0' :
        print("TERIMA KASIH :)\n")
        break

    else : #5210411227_REVY RAVLY SABBATHINO SAHETAPY
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......")