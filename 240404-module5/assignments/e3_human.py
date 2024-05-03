class Manusia(object):
    """ CLass dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self, nama):
        self.nama = nama
    def ucapkan_salam(self):
        print("Salam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya mau olahraga", k)
        self.keadaan = 'lapar'
    def mengalikan_dengan_dua(self, n):
        return n*2