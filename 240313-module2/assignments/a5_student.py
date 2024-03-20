from e3_human import Manusia
class Mahasiswa(Manusia):
    """ Class Mahasiswa yang dibangun dari class Manusia. """
    list_kuliah = []
    def __init__(self, nama, NIM, kota, uang_saku):
        """ Method inisiasi ini menutupi method inisiasi di class Manusia. """
        self.nama = nama
        self.NIM = NIM
        self.kota_tinggal = kota
        self.uang_saku = uang_saku
    def __str__(self):
        s = self.nama +', NIM '+ str(self.NIM) \
            +'. Tinggal di '+ self.kota_tinggal \
            +'. Uang saku Rp'+ str(self.uang_saku) \
            +' tiap bulannya.'
        return s
    def ambil_nama(self):
        return self.nama
    def ambil_NIM(self):
        return self.NIM
    def ambil_uang_saku(self):
        return self.uang_saku
    def makan(self, s):
        """  Metode ini menutupi metode 'makan'-nya class Manusia. Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'
    def ambil_kuliah(self, mata_kuliah):
        if mata_kuliah in self.list_kuliah:
            print(mata_kuliah, ' sudah diambil')
        else:
            self.list_kuliah.append(mata_kuliah)
    def hapus_kuliah(self, mata_kuliah):
        if mata_kuliah in self.list_kuliah:
            self.list_kuliah.remove(mata_kuliah)
        else:
            print(mata_kuliah, ' tidak diambil')

m234 = Mahasiswa('Gege', 777, 'Malang', 750000)
print(m234.list_kuliah)
m234.ambil_kuliah('Matematika Diskrit')
print(m234.list_kuliah)
m234.ambil_kuliah('Algoritma dan Struktur Data')
print(m234.list_kuliah)
m234.hapus_kuliah('Matematika Diskrit')
print(m234.list_kuliah)

print("\nProgram Completed!\n\n--- By L200220277 ---")