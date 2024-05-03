from a7_studenttif import daftar
def pencarian_uang_sedikit (data):
    mahasiswa = []
    for i in data:
        if 250000 > i.uang_saku:
            mahasiswa.append(i.__dict__)
    return mahasiswa

print(pencarian_uang_sedikit(daftar))

print("\nProgram Completed!\n\n--- By L200220277 ---")