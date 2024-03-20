from e4_student import Mahasiswa
class MhsTIF(Mahasiswa):
    """ Class MhsTIF yang dibangun dari class Mahasiswa. """
    def katakan_py(self):
        print('Python is cool.')

a = MhsTIF('Doni', 2327, 'Klaten', 350000)
print(a.keadaan)
print(a.nama)
print(a.kota_tinggal)
print(a.ambil_NIM())
print(a.ambil_nama())
print(a.ambil_uang_saku())
a.katakan_py()
a.makan('sate')
print(a.mengalikan_dengan_dua(23))
print("\nProgram Completed!\n\n--- By L200220277 ---")