from math import sqrt

def selesaikan_abc(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D < 0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real."
    x1 = (-b + sqrt(D))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    hasil = (x1, x2)
    return hasil

print(selesaikan_abc(1, 2,3))
print("\nProgram Completed!\n\n--- By L200220277 ---")