from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(1, n+1):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

def BFS2(G, src, dest):
    Q = deque([src])
    marked = {}
    path = []

    while len(Q) != 0:
        current_node = Q.popleft()
        if current_node == dest:
            path.append(current_node)
            return path

        if current_node not in marked:
            path.append(current_node)
            marked[current_node] = True
            for node in G.adj[current_node]:
                Q.append(node)

    return []



def BFS3(G, src):
    Q = deque([src])
    marked = {}
    pDict = {}

    while len(Q) > 0:
        current_node = Q.popleft()
        if current_node not in marked: 
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node not in marked:
                    pDict[node] = current_node
                    Q.append(node)

    return pDict


def is_connected(G):
    if len(G.adj) != 0:
        pDict = BFS3(G, 0)
        if(len(pDict) + 1 != len(G.adj)):
            return False

    return True

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


g = Graph(6)
g.add_edge(1,3)
g.add_edge(1,2)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(4,6)


print(BFS3(g, 1))

print(is_connected(g))



