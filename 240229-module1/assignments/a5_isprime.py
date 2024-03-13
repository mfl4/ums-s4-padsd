from math import sqrt
def apakah_prima(n):
    n = int(n)
    assert n>=0
    prima_kecil = [2,3,5,7,11]
    bukan_pr_kecil = [0,1,4,6,8,9,10]
    if n in prima_kecil:
        return True
    elif n in bukan_pr_kecil:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True


# print(apakah_prima(24))
# print(apakah_prima(17))
# print(apakah_prima(97))
# print(apakah_prima(123))