def gabungkan_arr_urut(arr1, arr2):
    arr = arr1 + arr2
    n = len(arr)
    for i in range(1, n):
        nilai = arr[i]
        pos = i
        while pos > 0 and nilai < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = nilai
    return arr


A = [1, 9, 8, 7, 11]
B = [4, 6, 2, 12, 10]

C = gabungkan_arr_urut(A, B)
print("Merged Sorted Array:", C)
