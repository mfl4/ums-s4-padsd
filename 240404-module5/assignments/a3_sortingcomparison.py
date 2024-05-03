from time import time as detak
from random import shuffle as kocok
from e3_bubblesort import bubble_sort
from e4_selectionsort import selection_sort
from e5_insertionsort import insertion_sort
k = list(range(1,6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
aw = detak(); bubble_sort(u_bub); ak = detak(); print('Bubble Sort: %g detik' %(ak - aw))
aw = detak(); selection_sort(u_sel); ak = detak(); print('Selection Sort: %g detik' %(ak - aw))
aw = detak(); insertion_sort(u_ins); ak = detak(); print('Insertion Sort: %g detik' %(ak - aw))
