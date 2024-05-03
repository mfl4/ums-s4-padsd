from e2_smallestposition import cari_posisi_yang_terkecil
from e1_swap import swap


def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        index_kecil = cari_posisi_yang_terkecil(A, i, n)
        if index_kecil != i:
            swap(A, i, index_kecil)
