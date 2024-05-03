class ArrayMatrix:
    def __init__(self, matriks):
        self.matriks = matriks

    def cek_konsistensi(self):
        valid_types = (int, float)
        for baris in self.matriks:
            for elemen in baris:
                if type(elemen) not in valid_types:
                    return False
        return all(len(baris) == len(self.matriks[0]) for baris in self.matriks)

    def dapatkan_ukuran(self):
        baris = len(self.matriks)
        kolom = len(self.matriks[0]) if self.matriks else 0
        return baris, kolom

    def tambah(self, matriks_lain):
        if not self.cek_konsistensi() or not matriks_lain.cek_konsistensi():
            print("Ukuran matriks tidak konsisten")
        hasil = []
        for i in range(len(self.matriks)):
            baris_hasil = []
            for j in range(len(self.matriks[0])):
                baris_hasil.append(self.matriks[i][j] + matriks_lain.matriks[i][j])
            hasil.append(baris_hasil)
        return ArrayMatrix(hasil)

    def kali(self, matriks_lain):
        if len(self.matriks[0]) != len(matriks_lain.matriks):
            print("Ukuran matriks tidak kompatibel untuk perkalian")

        hasil = []
        for i in range(len(self.matriks)):
            baris_hasil = []
            for j in range(len(matriks_lain.matriks[0])):
                jumlah = 0
                for k in range(len(self.matriks[0])):
                    jumlah += self.matriks[i][k] * matriks_lain.matriks[k][j]
                baris_hasil.append(jumlah)
            hasil.append(baris_hasil)
        return ArrayMatrix(hasil)

    def determinan(self):
        n = len(self.matriks)
        if n == 1:
            return self.matriks[0][0]
        if n == 2:
            return self.matriks[0][0] * self.matriks[1][1] - self.matriks[0][1] * self.matriks[1][0]
        hasil = 0
        tanda = 1
        for c in range(len(self.matriks[0])):
            submatriks = [baris[:c] + baris[c+1:] for baris in self.matriks[1:]]
            subdeterminan = ArrayMatrix(submatriks).determinan()
            hasil += tanda * self.matriks[0][c] * subdeterminan
            tanda *= -1
        return hasil

matriks1 = ArrayMatrix([[1.9, 2, 3.8], [4, 5.3, 6], [7.2, 8, 9.6]])
matriks2 = ArrayMatrix([[7,8.5, 9], [4.1, 5, 6.8], [1, 2.7, 3]])

print(matriks1.cek_konsistensi())
print(matriks1.dapatkan_ukuran())

hasil_tambah = matriks1.tambah(matriks2)
print(hasil_tambah.matriks)

hasil_kali = matriks1.kali(matriks2)
print(hasil_kali.matriks)
print(matriks1.determinan())

print("\nProgram Completed!\n\n--- By L200220277 ---")
