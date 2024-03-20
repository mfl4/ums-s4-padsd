class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuah_string):
        self.teks = sebuah_string
    def cetak_ini(self):
        print(self.teks)
    def cetak_pakai_huruf_kapital(self):
        print(str.upper(self.teks))
    def cetak_pakai_huruf_kecil(self):
        print(str.lower(self.teks))
    def jumlah_karakter(self):
        return len(self.teks)
    def cetak_jumlah_karakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, string_baru):
        self.teks = string_baru
    def apakah_terkandung(self,teks_lain):
        return teks_lain.lower() in self.teks.lower()
    def hitung_konsonan(self):
        i = 0
        for huruf in self.teks:
            if huruf.lower() not in 'aiueo':
                i += 1
        return i
    def hitung_vokal(self):
        i = 0
        for huruf in self.teks:
            if huruf.lower() in 'aiueo':
                i += 1
        return i

# (a)
p9 = Pesan('Indonesia adalah negeri yang indah.')
print(p9.apakah_terkandung('ege'))
print(p9.apakah_terkandung('eka'))

# (b)
p10 = Pesan('Surakarta')
print(p10.hitung_konsonan())
print(p10.hitung_vokal())

print("\nProgram Completed!\n\n--- By L200220277 ---")