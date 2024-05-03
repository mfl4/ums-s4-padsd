def cari_posisi_yang_terkecil(A, dari_sini, sampai_sini):
    posisi_yang_terkecil = dari_sini           #-> anggap ini yang terkecil
    for i in range(dari_sini+1, sampai_sini): #-> cari di sisa list
        if A[i] < A[posisi_yang_terkecil]:    #-> kalau menemukan yang lebih kecil,
            posisi_yang_terkecil = i          #-> anggapan dirubah
    return posisi_yang_terkecil

A = [18, 13, 44, 25, 66, 107, 78, 89]
j = cari_posisi_yang_terkecil(A, 2, len(A))
print(f"Smallest position of {A} is {A[j]} in {j}")