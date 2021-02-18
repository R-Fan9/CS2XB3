import random
import math
import timeit
def swap(L, f, s):
    temp = L[f]
    L[f] = L[s]
    L[s] = temp

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L, i)

def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i, i-1)
        else:
            return
        i -= 1

def selection_sort(L):
    for i in range(len(L)):
        minDex = find_min_index(L, i)
        swap(L, i, minDex)

def find_min_index(L, n):
    minDex = n
    for i in range(n+1, len(L)):
        if L[i] < L[minDex]:
            minDex = i
        
    return minDex



def middleOfThree(a, b, c): 
    # Compare each three number to find  
    # middle number. Enter only if a > b 
    if a > b :  
        if (b > c): 
            return b 
        elif (a > c) : 
            return c 
        else : 
            return a  
    else: 
        # Decided a is not greater than b. 
        if (a > c) : 
            return a 
        elif (b > c) : 
            return c 
        else : 
            return b 

def quad_pivot_quicksort(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L), max(L)]
    elif len(L) < 4:
        return [min(L), middleOfThree(L[0], L[1], L[2]), max(L)]
    else:
        ft = [L[0],L[1],L[2],L[3]]
        ft.sort()
        p1 = ft[0]
        p2 = ft[1]
        p3 = ft[2]
        p4 = ft[3]

        fst, scd, thd, fth, fiv = [], [], [], [], []

        for num in L[4:]:
            if(num < p1):
                fst.append(num)
            elif(num < p2):
                scd.append(num)
            elif(num < p3):
                thd.append(num)
            elif(num < p4):
                fth.append(num)
            else:
                fiv.append(num)
        return (quad_pivot_quicksort(fst) + [p1] + 
        quad_pivot_quicksort(scd) + [p2] + 
        quad_pivot_quicksort(thd) + [p3] +
        quad_pivot_quicksort(fth) + [p4] +
        quad_pivot_quicksort(fiv))

def dual_pivot_quicksort(L):
    if len(L) < 2:
        return L

    pivot1=min(L[0],L[1])
    pivot2=max(L[0],L[1])

    fst, scd, thd = [], [], []

    for num in L[2:]:
        if(num < pivot1):
            fst.append(num)
        elif(num < pivot2):
            scd.append(num)
        else:
            thd.append(num)
    return dual_pivot_quicksort(fst) + [pivot1] + dual_pivot_quicksort(scd) + [pivot2] + dual_pivot_quicksort(thd)

def final_sort_dual(L):
    if(len(L) < 2):
        return L
    elif(len(L) < 6):
        insertion_sort(L)
    else:
        pivot1=min(L[0],L[1])
        pivot2=max(L[0],L[1])

        fst, scd, thd = [], [], []

        for num in L[2:]:
            if(num < pivot1):
                fst.append(num)
            elif(num < pivot2):
                scd.append(num)
            else:
                thd.append(num)
        return dual_pivot_quicksort(fst) + [pivot1] + dual_pivot_quicksort(scd) + [pivot2] + dual_pivot_quicksort(thd)


def final_sort_quad_insert(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L), max(L)]
    elif len(L) < 4:
        return [min(L), middleOfThree(L[0], L[1], L[2]), max(L)]
    elif len(L) < 6:
        insertion_sort(L)
    else:
        ft = [L[0],L[1],L[2],L[3]]
        ft.sort()
        p1 = ft[0]
        p2 = ft[1]
        p3 = ft[2]
        p4 = ft[3]

        fst, scd, thd, fth, fiv = [], [], [], [], []

        for num in L[4:]:
            if(num < p1):
                fst.append(num)
            elif(num < p2):
                scd.append(num)
            elif(num < p3):
                thd.append(num)
            elif(num < p4):
                fth.append(num)
            else:
                fiv.append(num)
        return (quad_pivot_quicksort(fst) + [p1] + 
        quad_pivot_quicksort(scd) + [p2] + 
        quad_pivot_quicksort(thd) + [p3] +
        quad_pivot_quicksort(fth) + [p4] +
        quad_pivot_quicksort(fiv))


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def timetest(runs, length, sort):
    total = 0
    for _ in range(runs):
        L = create_random_list(length)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs


for i in range(1, 11, 1):
    print(i, timetest(1000, i, bubble_sort), 
    timetest(1000, i, selection_sort), 
    timetest(1000, i, insertion_sort), 
    timetest(1000, i, quad_pivot_quicksort),
    timetest(1000, i, dual_pivot_quicksort))


