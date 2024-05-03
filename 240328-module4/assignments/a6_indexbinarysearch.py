def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

data = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
angka = 9
hasil = binSe(data, angka)
if hasil:
    print(f"Angka {angka} ditemukan pada indeks ke-{hasil} data ini")
else:
    print(f"Angka {angka} tidak ditemukan pada data ini")


print("\nProgram Completed!\n\n--- By L200220277 ---")