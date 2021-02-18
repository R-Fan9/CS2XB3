import random
import math
import timeit
import sys
import numpy
from sort import *

# traditional quicksort
def my_quicksort(L):
    # return quicksort_copy(L)
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

def swap(L, f, s):
    temp = L[f]
    L[f] = L[s]
    L[s] = temp

# bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

# insertion sort
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

# selection sort
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

# testing whether the multi-pivot quicksorts produce the same results as the
# traditional and inplace quicksorts
def test_multi_pivot_sorts():
     for i in range(10000):
        L = create_random_list(i)
        aCopy=L.copy()
        bCopy=L.copy()
        my_quicksort(aCopy)
        quicksort_inplace(bCopy)
        c=dual_pivot_quicksort(L.copy())
        d=tri_pivot_quicksort(L.copy())
        e=quad_pivot_quicksort(L.copy())

        assert(aCopy==bCopy==c==d==e)

# main function used to collect data-points for graphs
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

# used for testing final_sort
def timetest(runs, length, sort):
    total = 0
    for _ in range(runs):
        L = create_random_list(length)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# used for testing quicksorts with near-sorted lists as inputs
def time_near_sort(runs,n,f,factor):
    for i in range(0,n):
        totatime = 0
        L=create_near_sorted_list(i,factor)
        for run in range(runs):
            start = timeit.default_timer()
            f(L)
            end = timeit.default_timer()
            totatime+=end-start
        print(totatime/runs)

# used for testing how near-sorted factor affects the performance of quicksorts
def time_different_factors(runs,f):
    for i in numpy.arange(0, 0.1, 0.001):
        totatime = 0
        L=create_near_sorted_list(1000,i)
        for run in range(runs):
            start = timeit.default_timer()
            f(L)
            end = timeit.default_timer()
            totatime+=end-start
        print(totatime/runs)

# used for testing quicksorts with reverse-sorted lists as inputs
def time_reverse_sort(runs,n,f):
    for i in range(1,n):
        totatime = 0
        L=create_random_list(i)
        L.sort()
        L=L[::-1]
        for run in range(runs):
            start = timeit.default_timer()
            f(L)
            end = timeit.default_timer()
            totatime+=end-start
        print(totatime/runs)

# test_multi_pivot_sorts()

# sys.stdout = open('my_quick_sort_with_no_replacements_15r_650n', 'w')
# time(15,600,my_quicksort)

# sys.stdout = open('quicksort_inplace_15r_650n', 'w')
#time(15,650,quicksort_inplace)

# sys.stdout = open('dual_pivot_quicksort_20r_1000n', 'w')
# time(20,1000,dual_pivot_quicksort)

# sys.stdout = open('tri_pivot_quicksort_20r_1000n', 'w')
# time(20,1000,tri_pivot_quicksort

# sys.stdout = open('i_1000', 'w')
# for i in range(1000):
#     print(i)

# sys.stdout = open('bubble_avg', 'w')
# time(15,600,bubble_sort)
# sys.stdout = open('insert_avg', 'w')
# time(15,600,insertion_sort)
# sys.stdout = open('select_avg', 'w')
# time(15,600,selection_sort)
# sys.stdout = open('quad_avg', 'w')
# time(15,600,quad_pivot_quicksort)

# sys.stdout = open('bubble_avg_f0.01', 'w')
# time_near_sort(5,1000,bubble_sort,0.01)
# sys.stdout = open('insert_avg_f0.01', 'w')
# time_near_sort(5,1000,insertion_sort,0.01)
# sys.stdout = open('select_avg_f0.01', 'w')
# time_near_sort(5,1000,selection_sort,0.01)
# sys.stdout = open('quad_avg_f0.01', 'w')
# time_near_sort(5,1000,quad_pivot_quicksort,0.01)

# sys.stdout = open('i_0.01-1', 'w')
# for i in numpy.arange(0, 1, 0.01):
#     print(i)

# sys.stdout = open('i_0.001-0.1', 'w')
# for i in numpy.arange(0, 0.1, 0.001):
#     print(i)

# sys.stdout = open('bubble_factor_test', 'w')
# time_different_factors(5,bubble_sort)
# sys.stdout = open('insert_factor_test', 'w')
# time_different_factors(5,insertion_sort)
# sys.stdout = open('select_factor_test', 'w')
# time_different_factors(5,selection_sort)
# sys.stdout = open('quad_factor_test', 'w')
# time_different_factors(5,quad_pivot_quicksort)

# sys.stdout = open('bubble_reverse', 'w')
# time_reverse_sort(15,600,bubble_sort)
# sys.stdout = open('insert_reverse', 'w')
# time_reverse_sort(15,600,insertion_sort)
# sys.stdout = open('select_reverse', 'w')
# time_reverse_sort(15,600,selection_sort)
# sys.stdout = open('quad_reverse', 'w')
# time_reverse_sort(15,600,quad_pivot_quicksort)

# sys.stdout = open('quad_best_test', 'w')
# time(20,1000,quad_quicksort)
# sys.stdout = open('final_quicksort_best_test', 'w')
# time(20,1000, final_sort)

# sys.stdout = open('final_sort_vs_quad', 'w')
# for i in range(0, 1000, 50):
#     print(i,
#     timetest(1000, i, quad_pivot_quicksort),
#     timetest(1000, i, final_sort))

# sys.stdout = open('final_worst', 'w')
# time_reverse_sort(15,1000, final_sort)