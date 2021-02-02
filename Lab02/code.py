import timeit



def test_copy_time(alist):
    start = timeit.default_timer()
    alist.copy()
    end = timeit.default_timer()
    time = end - start
    return time

def generate_list(n):
    alist = [i for i in range(n)]
    return alist

def test_copy(numOfRuns, maxSize):

    for x in range(maxSize):

        alist = generate_list(x)
        totalTimeForOneSize = 0

        for y in range(numOfRuns):
            totalTimeForOneSize += test_copy_time(alist)

        print(x, totalTimeForOneSize/numOfRuns)



#test_copy(1000, 1000)


def test_lookup_time(alist, index):
    start = timeit.default_timer()
    alist[index]
    end = timeit.default_timer()
    time = end - start
    return time


def test_lookup(numOfRuns):
    alist = [i for i in range(1000000)]
    for i in range(len(alist)):
        totalTime = 0

        for j in range(numOfRuns):
            totalTime += test_lookup_time(alist, i)

        print(i, totalTime/numOfRuns)

test_lookup(1000)




