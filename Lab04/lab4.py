import random


def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def time(runs,n,f):
    for i in range(0,n):
        totatime = 0
        L=create_random_list(i)
        for run in range(runs):
            # print(L)
            start = timeit.default_timer()
            f(L)
            end = timeit.default_timer()
            totatime+=end-start
            # print(L)
        print(totatime/runs)


def test_sorts():
    for i in range(10000):
        L = create_random_list(i)
        aCopy=L.copy()
        bCopy=L.copy()
        cCopy=L.copy()
        mergesort_bottom(aCopy)
        mergesort_three_way(bCopy)
        mergesort(cCopy)

        assert(aCopy==bCopy==cCopy)
    print("Done")
