from a5_isprime import apakah_prima
def cek_prima():
    angka_prima = []
    for i in range(2, 1000):
        if apakah_prima(i):
            angka_prima.append(i)
    return angka_prima
print(cek_prima())
print("\nProgram Completed!\n\n--- By L200220277 ---")