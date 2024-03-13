def faktor_prima(n):
    faktor = []
    pembagi = 2
    while n > 1:
        while n % pembagi == 0:
            faktor.append(pembagi)
            n //= pembagi
        pembagi += 1
    return tuple(faktor)

print(faktor_prima(10))
print(faktor_prima(120))
print(faktor_prima(19))
print("\nProgram Completed!\n\n--- By L200220277 ---")