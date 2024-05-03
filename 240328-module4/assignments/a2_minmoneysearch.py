from a7_studenttif import daftar
def pencarian_uang (data):
    uang = data[0].uang_saku
    for i in data:
        if uang > i.uang_saku:
            uang = i.uang_saku
    return uang

print(pencarian_uang(daftar))

print("\nProgram Completed!\n\n--- By L200220277 ---")