from e1_swap import swap
from a7_studenttif import daftar
def urutkan_mahasiswa(mahasiswa):
    n = len(mahasiswa)
    for i in range(n-1):
        for j in range(n-i-1):
            if mahasiswa[j].NIM > mahasiswa[j+1].NIM:
                swap(mahasiswa, j, j + 1)
    return mahasiswa

umd = urutkan_mahasiswa(daftar)
for i in umd:
    print(i)
