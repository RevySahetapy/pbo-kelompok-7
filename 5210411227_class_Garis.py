class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Garis:
    def __init__(self, titik_pertama, titik_kedua):
        self.titik_pertama = titik_pertama
        self.titik_kedua = titik_kedua

    def panjang(self):
        panjangX = self.titik_kedua.x - self.titik_pertama.x
        panjangY = self.titik_kedua.y - self.titik_pertama.y
        panjang = (panjangX**2 + panjangY**2) ** 0.5
        return panjang


titik_C = Titik(0, 0)
titik_D = Titik(3, 4)
garis_CD = Garis(titik_C, titik_D)
print('Panjang garis CD adalah {}'.format(garis_CD.panjang()))
