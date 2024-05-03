def binSe(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            temp.append(mid)
            left = mid - 1
            while left >= 0 and kumpulan[left] == target:
                temp.append(left)
                left -= 1
            right = mid + 1
            while right < len(kumpulan) and kumpulan[right] == target:
                temp.append(right)
                right += 1
            return temp
        elif kumpulan[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

data = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
angka = 6
hasil = binSe(data, angka)
if hasil:
    print(f"Angka {angka} ditemukan pada indeks {hasil} data ini")
else:
    print(f"Angka {angka} tidak ditemukan pada data ini")

print("\nProgram Completed!\n\n--- By L200220277 ---")