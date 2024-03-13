def gambarlah_persegi_empat(tinggi, lebar):
    for i in range(tinggi):
        for j in range(lebar):
            if i == 0 or i == tinggi - 1 or j == 0 or j == lebar - 1:
                print("@", end="")
            else:
                print(" ", end="")
        print()

gambarlah_persegi_empat(4, 5)
print("\nProgram Completed!\n\n--- By L200220277 ---")