import random
import timeit
import math
import numpy
import sys
from sorts import *

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
            start = timeit.default_timer()
            f(L)
            end = timeit.default_timer()
            totatime+=end-start
        print(totatime/runs)

def time_different_factors(runs,f):
    for i in numpy.arange(0, 0.5, 0.001):
        totatime = 0
        L=create_near_sorted_list(1000,i)
        for run in range(runs):
            start = timeit.default_timer()
            f(L)
            end = timeit.default_timer()
            totatime+=end-start
        print(totatime/runs)

def test_sorts():
    for i in range(10000):
        L = create_random_list(i)
        aCopy=L.copy()
        bCopy=L.copy()
        cCopy=L.copy()
        mergesort_bottom(aCopy)
        mergesort_three(bCopy)
        mergesort(cCopy)
        assert(aCopy==bCopy==cCopy)
    print("Done")

# sys.stdout = open('traditional_merge_sort', 'w')
# time(15,1000,mergesort)
# sys.stdout = open('three_way_merge_sort', 'w')
# # time(15,1000,mergesort_three)
# sys.stdout = open('bottom_up_merge_sort', 'w')
# time(15,1000,mergesort_bottom)

# sys.stdout = open('i_0-0.5', 'w')
# for i in numpy.arange(0, 0.5, 0.001):
#     print(i)
# sys.stdout = open('bottom_up_factor_test', 'w')
# time_different_factors(50,mergesort_bottom)
