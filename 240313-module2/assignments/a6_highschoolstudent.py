from e3_human import Manusia
class SiswaSMA(Manusia):
    """ Class SiswaSMA yang dibangun dari class Manusia. """
    def __init__(self, nama, NP, kelas):
        """ Method inisiasi ini menutupi method inisiasi di class Manusia. """
        self.nama = nama
        self.NP = NP
        self.kelas = kelas
    def __str__(self):
        teks = self.nama +', NIM '+ self.NP +\
            +'. sekarang kelas '+ self.kelas
        return teks
    def ambil_nama(self):
        return self.nama
    def perbarui_nama(self, nama_baru):
        self.nama = nama_baru
    def ambil_NP(self):
        return self.NP
    def perbarui_NP(self, NP_baru):
        self.NP = NP_baru
    def ambil_kelas(self):
        return self.kelas
    def perbarui_kelas(self, kelas_baru):
        self.kelas = kelas_baru

s1 = SiswaSMA('Fre', 'L200220277', 'C')
print(s1.ambil_nama())
print(s1.ambil_NP())
print(s1.ambil_kelas())
s1.perbarui_nama('Freya')
s1.perbarui_NP('L200220777')
s1.perbarui_kelas('X')
print(s1.ambil_nama())
print(s1.ambil_NP())
print(s1.ambil_kelas())

print("\nProgram Completed!\n\n--- By L200220277 ---")