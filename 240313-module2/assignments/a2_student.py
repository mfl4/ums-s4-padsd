from e3_human import Manusia
class Mahasiswa(Manusia):
    """ Class Mahasiswa yang dibangun dari class Manusia. """
    def __init__(self, nama, NIM, kota, uang_saku):
        """ Method inisiasi ini menutupi method inisiasi di class Manusia. """
        self.nama = nama
        self.NIM = NIM
        self.kota_tinggal = kota
        self.uang_saku = uang_saku
    def __str__(self):
        s = self.nama +', NIM '+ str(self.NIM) \
            +'. Tinggal di '+self.kota_tinggal \
            +'. Uang saku Rp'+str(self.uang_saku) \
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
    def ambil_kota_tinggal(self):
        return self.kota_tinggal
    def perbarui_kota_tinggal(self, kota_baru):
        self.kota_tinggal = kota_baru
    def tambah_uang_saku(self, uang_tambahan):
        self.uang_saku = self.uang_saku + uang_tambahan

m9 = Mahasiswa('Ege', 123, 'Surabaya', 250000)

# (a)
print(m9.ambil_kota_tinggal())

# (b)
m9.perbarui_kota_tinggal('Sleman')
print(m9.ambil_kota_tinggal())

# (c)
m7 = Mahasiswa('Eka', 123, 'Surabaya', 270000)
print(m7.ambil_uang_saku())
m7.tambah_uang_saku(50000)
print(m7.ambil_uang_saku())

print("\nProgram Completed!\n\n--- By L200220277 ---")