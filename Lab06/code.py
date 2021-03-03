import random
import timeit
import sys

from rbt import *
tree = RBTree()
def test_height():
    global tree
    tree = RBTree()
    for i in range(1):
        for i in range(1,9):
            tree.insert(i)
        print(tree.get_height())

test_height()