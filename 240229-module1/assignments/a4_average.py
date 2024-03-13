def rerata(b):
    jumlah = 0
    for i in b:
        jumlah += i
    hasil = jumlah / len(b)
    return hasil

print(rerata([1,2,3,4,5]))
g = [3,4,5,4,3,4,5,2,2,10,11,23]
print(rerata(g))