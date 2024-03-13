from random import randint

def tebak_angka():
    angka_acak = randint(1, 100)
    tebakan = 0
    print("Permainan tebak angka.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
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

tebak_angka()
print("\nProgram Completed!\n\n--- By L200220277 ---")