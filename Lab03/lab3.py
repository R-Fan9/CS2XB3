import random
import math
import timeit

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]



def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def quicksort_inplace(L):
    my_quicksort_inplace(L,0,len(L)-1)
    
def my_quicksort_inplace(L,low,high):
    if low<high:
        p_idx = partition(L,low,high)
        my_quicksort_inplace(L,low,p_idx-1)
        my_quicksort_inplace(L,p_idx+1,high)

def partition(L,low,high):
    index = low
    pivot = L[high]
    for i in range(low,high):
        if L[i] <=  pivot:
            L[index], L[i] = L[i], L[index]
            index +=1
    L[index], L[high] = L[high], L[index]
    return index

def time(runs,n):
    for i in range(0,n):
        totatime = 0
        L=create_random_list(i)
        for run in range(runs):
            # print(L)
            start = timeit.default_timer()
            my_quicksort(L)
            end = timeit.default_timer()
            totatime+=end-start
            # print(L)
        print(i,totatime/runs)

#time(10,650)


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

def tri_pivot_quicksort(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L), max(L)]
    else:
        ft = [L[0],L[1],L[2]]
        ft.sort()
        pivot1=ft[0]
        pivot2=ft[1]
        pivot3=ft[2]
        fst, scd, thd, fth = [], [], [], []

        for num in L[3:]:
            if(num < pivot1):
                fst.append(num)
            elif(num < pivot2):
                scd.append(num)
            elif(num < pivot3):
                thd.append(num)
            else:
                fth.append(num)

        return (tri_pivot_quicksort(fst) + [pivot1] + 
        tri_pivot_quicksort(scd) + [pivot2] + 
        tri_pivot_quicksort(thd) + [pivot3] +
        tri_pivot_quicksort(fth))

def middleOfThree(a, b, c) : 
      
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


print(quad_pivot_quicksort([5,4,3,2,1]))
