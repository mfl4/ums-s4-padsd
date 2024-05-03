class MatrixListComprehension(object):
    def buat_nol(self, m, n=None):
        if n is None:
            n = m
        return [[0 for _ in range(n)] for _ in range(m)]
    def buat_identitas(self, m):
        return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

matriks = MatrixListComprehension()

matriksmxn = matriks.buat_nol(8, 5)
print(matriksmxn)

matriksm = matriks.buat_nol(4)
print(matriksm)

matriksid = matriks.buat_identitas(5)
print(matriksid)

print("\nProgram Completed!\n\n--- By L200220277 ---")