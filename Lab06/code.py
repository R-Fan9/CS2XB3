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

bst = BST()
tree = RBTree()
def test_height():
    global tree
    tree = RBTree()

    for i in range(3):
        for j in range(1,10001):
            tree.insert(j)
            bst.insert(j)

        print(tree.get_height())

test_height()

