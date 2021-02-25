import random
import timeit
import sys

from heap import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def test_building_heaps():
    for i in range(1,1000):
        L = create_random_list(i)
        x=Heap(L.copy(),1).is_heap()
        y=Heap(L.copy(),2).is_heap()
        z=Heap(L.copy(),3).is_heap()
        v=Heap(L.copy(),4).is_heap()
        assert(x==y==z==v)
    print("Test passed")

def time_heap(runs,n, build_option):
    for i in range(1,n+1,10):
        totatime = 0
        L=create_random_list(i)
        for run in range(runs):
            start = timeit.default_timer()
            Heap(L,build_option)
            end = timeit.default_timer()
            totatime+=end-start
        print(totatime/runs)

# test_building_heaps()


# sys.stdout = open('n_1_10000', 'w')
# for i in range(1,10000,10):
#     print(i)

# sys.stdout = open('heap_1', 'w')
# time_heap(15,10000, 1)
# sys.stdout = open('heap_2', 'w')
# time_heap(15,10000, 2)
# sys.stdout = open('heap_3', 'w')
# time_heap(15,10000, 3)
# sys.stdout = open('heap_3_modified', 'w')
# time_heap(15,10000, 4)
