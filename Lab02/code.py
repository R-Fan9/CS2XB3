import timeit
<<<<<<< HEAD


=======
import random
from enum import Enum, auto
>>>>>>> 9ccaf980126df5fba0f995da5f0503478035de11

def test_copy_time(alist):
    start = timeit.default_timer()
    alist.copy()
    end = timeit.default_timer()
    time = end - start
    return time

def generate_list(n):
    alist = [i for i in range(n)]
    return alist

<<<<<<< HEAD
def test_copy(numOfRuns, maxSize):
=======
def test_copy(numOfRuns, maxSize): # main function for testing copy() time
>>>>>>> 9ccaf980126df5fba0f995da5f0503478035de11

    for x in range(maxSize):

        alist = generate_list(x)
        totalTimeForOneSize = 0

        for y in range(numOfRuns):
            totalTimeForOneSize += test_copy_time(alist)

        print(x, totalTimeForOneSize/numOfRuns)

<<<<<<< HEAD


#test_copy(1000, 1000)


=======
#test_copy(1000, 1000)

>>>>>>> 9ccaf980126df5fba0f995da5f0503478035de11
def test_lookup_time(alist, index):
    start = timeit.default_timer()
    alist[index]
    end = timeit.default_timer()
    time = end - start
    return time

<<<<<<< HEAD

def test_lookup(numOfRuns):
=======
def test_lookup(numOfRuns):  # main function for testing lookup time
>>>>>>> 9ccaf980126df5fba0f995da5f0503478035de11
    alist = [i for i in range(1000000)]
    for i in range(len(alist)):
        totalTime = 0

        for j in range(numOfRuns):
            totalTime += test_lookup_time(alist, i)

        print(i, totalTime/numOfRuns)

<<<<<<< HEAD
test_lookup(1000)




=======
# test_lookup(1000)

def time_append(alist, elem):
    start = timeit.default_timer()
    alist.append(elem)
    end = timeit.default_timer()
    time = end - start
    return time

def test_append(runs):  # main function for testing append() time
    alist=[]
    for num in range(1000000):
        total_time_for_one_append = 0
        for i in range(runs):
            total_time_for_one_append += time_append(alist, 1)
            alist.pop()
        alist.append(1)
        print(num, total_time_for_one_append/runs)

# test_append(1)

# test_append(100)

class Shape(Enum): 
    circle = auto()
    triangle = auto()
    square = auto() 

randomElements = [100, Shape.square, "Hello", 20.3, True, Shape.circle, 200000, Shape.triangle, "Bye"]

def test_append2(runs): # additional function for testing append() time
    alist=[]
    for num in range(1000000):
        total_time_for_one_append = 0
        randomElem = randomElements[random.randint(0,len(randomElements) - 1)]
        for i in range(runs):
            total_time_for_one_append += time_append(alist, randomElem)
            alist.pop()
        alist.append(randomElem)
        print(num, total_time_for_one_append/runs)

# test_append2(1)

# test_append2(100)
>>>>>>> 9ccaf980126df5fba0f995da5f0503478035de11
