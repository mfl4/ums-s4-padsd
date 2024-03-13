def apakah_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

print(apakah_kabisat(1896))
print(apakah_kabisat(1897))
print(apakah_kabisat(1900))
print(apakah_kabisat(2000))
print(apakah_kabisat(2004))
print(apakah_kabisat(2008))
print(apakah_kabisat(2012))
print(apakah_kabisat(2016))
print(apakah_kabisat(2096))
print(apakah_kabisat(2100))
print(apakah_kabisat(2200))
print(apakah_kabisat(2300))
print(apakah_kabisat(2400))
print("\nProgram Completed!\n\n--- By L200220277 ---")