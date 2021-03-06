import random
import sys
import math
import numpy
import sys


from rbt import *

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if(self.root == None):
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)
            
    def __insert(self, node, value):
        newNode = BSTNode(value)
        if value < node.value:
            if node.left == None: 
                node.left = newNode
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None: 
                node.right = newNode
                node.right.parent = node
            else:
                self.__insert(node.right, value)

    
    def get_height(self):
        if self.root == None:
            return 0
        return self.__get_height(self.root)


    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))
    
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

# testing if the height is decreasing as 10000 elements get inserted several times
def test_height_10000_3times():
    tree = RBTree()
    for k in range(3):
        for i in range(1,1001):
            tree.insert(i)
        print(k, tree.get_height())

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

# testing height of RBT vs height of BST for random list of length 10000
def test_height():
    diff = test_height_helper(10)
    return diff

# testing if RBT works as expected for inserting random elements
def test_rand_list():
    rbt = RBTree()
    n = create_random_list(999)
    for i in n:
        rbt.insert(i)
    return rbt

#testing near-factor for RBT vs BST
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

<<<<<<< HEAD
#sys.stdout = open('near_sort', 'w')
#test_near_factors(5)
# test_rand_list()

print(test_height())
=======
# sys.stdout = open('factor', 'w')
# test_near_factors(5)

# test_rand_list()

# print(test_height())
>>>>>>> ba94d5d5e797e6727fd253a24e2708ace0543c62

# test_height_10000_3times()    

# x = RBNode(20)
# x.left =  RBNode(3)
# x.left.left =  RBNode(1)
# print(x)

# tree= RBTree()
# tree.insert(20)
# tree.insert(3)
# tree.insert(1)  
# tree.insert(-2)  
# tree.insert(-22)
# tree.insert(-2222)
# print(tree)

# tree= RBTree()
# tree.insert(20)
# tree.insert(3)
# tree.insert(1)  
# tree.insert(-2)  
# tree.insert(-22)
# tree.insert(-2222)
# print(tree)

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
