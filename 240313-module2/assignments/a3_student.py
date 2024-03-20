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

input_name = input("Masukkan nama: ")
input_NIM = input("Masukkan NIM: ")
input_city = input("Masukkan kota: ")
input_uang_saku = input("Masukkan uang saku: ")
m1 = Mahasiswa(input_name, input_NIM, input_city, input_uang_saku)

print(m1.__str__())

print("\nProgram Completed!\n\n--- By L200220277 ---")