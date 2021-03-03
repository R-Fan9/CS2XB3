import random

from rbt import *
from bst import *
import math
import numpy

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

def test_height_10000_3times():
    tree = RBTree()
    for _ in range(3):
        for i in range(1,10001):
            tree.insert(i)
        print(tree.get_height())

def test_height_helper(runs):
    ttl_ht_bst = 0
    ttl_ht_rbt = 0
    for run in range(runs):
        bst = BST()
        rbt = RBTree()
        L=create_random_list(10000)
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
    n = create_random_list(999)
    for i in n:
        rbt.insert(i)
    return rbt


def test_near_factors(runs):
    for i in numpy.arange(0, 0.55, 0.005):
        ttl_ht_bst = 0
        ttl_ht_rbt = 0


        for run in range(runs):
            bst = BST()
            rbt = RBTree()
            L=create_near_sorted_list(901,i)

            for x in L:
                bst.insert(x)

            for y in L:
                rbt.insert(y)
            ttl_ht_bst += bst.get_height()
            ttl_ht_rbt += rbt.get_height()

        print(i, ttl_ht_bst/runs, ttl_ht_rbt/runs)

test_near_factors(5)
# test_rand_list()

#print(test_height())

# test_height_10000_3times()    

# x= RBNode(20)
# x.left =  RBNode(3)
# x.left.left =  RBNode(1)

# tree= RBTree()
# tree.insert(20)
# tree.insert(3)
# tree.insert(1)  
# tree.insert(-2)  
# tree.insert(-22)
# tree.insert(-2222)

# tree= RBTree()
# tree.insert(20)
# tree.insert(3)
# tree.insert(1)  
# tree.insert(-2)  
# tree.insert(-22)
# tree.insert(-2222)

# tree= RBTree()
# tree.insert(20)
# tree.insert(31)
# tree.insert(111)  
# tree.insert(2000)  
# tree.insert(5000)
# tree.insert(-2)

# tree = RBTree()
# tree.insert(100)
# tree.insert(400)
# tree.insert(200)
# tree.insert(300)
# tree.insert(350)
# tree.insert(375)
# tree.insert(325)
# tree.insert(325)
# tree.insert(150)
# tree.insert(135)
# tree.insert(75)
# str(tree) == "[[[[[(75,R)] <- (100,B)] <- (135,R) -> [(150,B)]] <- (200,B) -> [[[(300,R)] <- (325,B) -> [(325,R)]] <- (350,R) -> [[(375,R)] <- (400,B)]]]]"
