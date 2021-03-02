import math

class kHeap:
    length = 0
    data = []

    def __init__(self, values, k):
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap()

    def build_heap(self):
    
        for i in range(self.length // self.k - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        largest_known = i
        chd = self.children(i)
        max_value = self.data[i]
        for x in chd:
            if x < self.length and self.data[x] > max_value:
                max_value = self.data[x]
                largest_known = x
            else:
                break
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)    

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.sink(0)
        return max_value

    def children(self, i):
        chd = []
        for x in range(1, self.k+1):
            chd.append(i*self.k+x)
        return chd

    def parent(self, i):
<<<<<<< HEAD
        return 2 // self.k + (i - 1) // self.k

=======
        return math.ceil(i / (self.k)) - 1
>>>>>>> 32c6670216dd1570d56d1e87ff36c88fd505fae3
