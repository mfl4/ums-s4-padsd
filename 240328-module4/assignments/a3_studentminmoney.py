from a7_studenttif import daftar
def pencarian_mahasiswa (data):
    mahasiswa = []
    uang = data[0].uang_saku
    for i in data:
        if uang > i.uang_saku:
            uang = i.uang_saku
            mahasiswa.append(i.__dict__)
    return mahasiswa

print(pencarian_mahasiswa(daftar))

print("\nProgram Completed!\n\n--- By L200220277 ---")