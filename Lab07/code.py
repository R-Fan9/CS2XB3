import random
import sys

from graphs import *

def test_c(runs,f):
    graph = Graph(100)
    k=graph.number_of_nodes()
    for c in range(1000):
        passed_test = 0
        for run in range(runs):
            for i in range(c):
                all_connected, fst, scnd = get_possible_random_values_for_an_edge(graph,k)
                if all_connected:
                    break
                graph.add_edge(fst, scnd)
            if f(graph):
                passed_test += 1
            graph = Graph(100)
        print(c,passed_test/runs) 

# Guarantees to generate two random values that don't have an edge between them in the graph.
# Eliminates a possibility to generate two equal values.
def get_possible_random_values_for_an_edge(g,k):
    for node in g.adj:
        if  len(g.adj[node])+1 != len(g.adj):
            fst = random.randint(0, k-1)
            while len(g.adj[fst])+1 == len(g.adj):
                fst = random.randint(0, k-1)
            scnd = random.randint(0, k-1)
            while scnd == fst or scnd in g.adj[fst]:
                scnd = random.randint(0, k-1)
            return False, fst, scnd
    return True, 0, 0

# sys.stdout = open('cycles_vs_c', 'w')
# test_c(100,has_cycle)

# sys.stdout = open('is_connected_vs_c', 'w')
# test_c(100,is_connected)

# g2= Graph(0)
# g = Graph(10)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(1,5)
# g.add_edge(2,6)
# g.add_edge(2,7)
# g.add_edge(3,0)
# g.add_edge(3,7)     
# g.add_edge(5,4)
# g.add_edge(8,9)
# print(has_cycle(g))
# print(has_cycle(g2))
# print(DFS2(g,1,2))
# print(DFS2(g,1,0))
# print(DFS3(g,1))
# print(DFS3(g,2))

# g = Graph(6)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(3,4)
# g.add_edge(3,5)
# g.add_edge(4,5)
# g.add_edge(4,6)
# for node in g.adj:
#     print(node,g.adj[node])
# print(BFS3(g,1))
# print(DFS3(g,1))
