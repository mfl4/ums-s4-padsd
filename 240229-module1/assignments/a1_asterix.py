def cetak_siku(x):
    for i in range(x):
        for j in range(i+1):
            print("*", end=" ")
        print()

cetak_siku(5)