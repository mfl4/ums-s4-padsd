from a7_studenttif import daftar

def pencarian_linier(data, target):
    wadah = []
    for i in data:
        if i.kota_tinggal == target:
            wadah.append(data.index(i))
    return wadah

print(pencarian_linier(daftar, 'Boyolali'))
print("\nProgram Completed!\n\n--- By L200220277 ---")
