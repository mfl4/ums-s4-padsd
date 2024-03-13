def katakan(n):
    if n == 0:
        return "nol"
    elif n < 10:
        return ['satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan'][n-1]
    elif n < 20:
        return "belas " + katakan(n % 10)
    elif n < 100:
        return ['dua puluh', 'tiga puluh', 'empat puluh', 'lima puluh', 'enam puluh', 'tujuh puluh', 'delapan puluh', 'sembilan puluh'][n // 10 - 2] + (" " + katakan(n % 10) if n % 10 != 0 else "")
    elif n < 1000:
        return katakan(n // 100) + " ratus" + (" " + katakan(n % 100) if n % 100 != 0 else "")
    elif n < 1000000:
        return katakan(n // 1000) + " ribu" + (" " + katakan(n % 1000) if n % 1000 != 0 else "")
    elif n < 1000000000:
        return katakan(n // 1000000) + " juta" + (" " + katakan(n % 1000000) if n % 1000000 != 0 else "")
    else:
        return "Angka terlalu besar"

print(katakan(3125750))
print("\nProgram Completed!\n\n--- By L200220277 ---")