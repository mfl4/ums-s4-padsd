from random import randint
import math

def tebak_angka(awal, akhir):
    angka_acak = randint(awal, akhir)
    maks_tebakan = math.ceil(math.log2(akhir - awal + 1))
    tebakan = 0
    print("Permainan tebak angka.")
    print(f"Bilangan bulat ini terdapat diantara {awal} sampai {akhir}. Coba tebak.")
    while True:
        tebakan += 1
        angka_tebakan = int(input(f"Masukkan tebakan ke-{tebakan}:> "))
        if angka_tebakan < angka_acak:
            print("Itu terlalu kecil. Coba lagi.")
        elif angka_tebakan > angka_acak:
            print("Itu terlalu besar. Coba lagi.")
        else:
            print(f"Ya. Anda benar!")
            break
        if tebakan == maks_tebakan:
            print(f"Batas maksimum tebakan yaitu ({maks_tebakan}) tercapai. Jawabannya adalah {angka_acak}.")
            break

tebak_angka(1, 100)
print()
tebak_angka(1, 1000)

print("\nProgram Completed!\n\n--- By L200220277 ---")
