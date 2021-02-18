def mergesort_bottom(L):
    n = len(L)
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            merge_bottom(L, j, j+i-1, min(j+i+i-1, n-1))
            j = j + i + i
        i = i+i

def merge_bottom(L, start, mid, end):
    i = start
    j = mid+1

    a = [0 for i in L]
    for x in range(start, end+1):
        a[x] = L[x]

    for x in range(start, end+1):
        if i > mid:
            L[x] = a[j]
            j += 1
        elif j > end:
            L[x] = a[i]
            i += 1
        elif a[j] < a[i]:
            L[x] = a[j]
            j += 1
        else:
            L[x] = a[i]
            i += 1
