import random
import timeit
import sys

from rbt import *

tree = RBTree()

def test_height():
    global tree
    tree = RBTree()
    for _ in range(3):
        for i in range(1,10001):
            tree.insert(i)
        print(tree.get_height())

# test_height()

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