import random
import timeit
import sys

from rbt import *
from bst import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def test_height_helper(runs):
    ttl_ht_bst = 0
    ttl_ht_rbt = 0
    for run in range(runs):
        bst = BST()
        rbt = RBTree()
        L=create_random_list(10001)
        for i in L:
            bst.insert(i)
            rbt.insert(i)
        ttl_ht_bst += bst.get_height()
        ttl_ht_rbt += rbt.get_height()
        

    return abs(ttl_ht_bst/runs - ttl_ht_rbt/runs)


def test_height():
    diff = test_height_helper(10)
    return diff


def test_rand_list():
    rbt = RBTree()
    n = create_random_list(1001)
    for i in n:
        rbt.insert(i)

    return rbt

#print(test_height())

