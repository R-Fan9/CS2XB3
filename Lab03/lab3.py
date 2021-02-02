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

time(10,650)