from collections import deque

#Undirected graph using an adjacency list
class Graph:
    def __init__(self, n):
        self.adj = {}
        for i in range(n):
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

def BFS2(G, node1, node2):
    result =[]
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        result.append(current_node)
        for node in G.adj[current_node]:
            if node == node2:
                result.append(node)
                return result
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return []

def BFS3(G, node1):
    result = {}
    for node2 in G.adj:
        if node2 != node1 and BFS(G, node1,node2):
            path = BFS2(G, node1, node2)
            path.pop()
            result[node2]=path.pop()
    return result

def DFS2(G, node1, node2):
    result = []
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            result.append(current_node)
            for node in G.adj[current_node]:
                if node == node2:
                    result.append(node)
                    return result
                S.append(node)
    return []

def DFS3(G, node1):
    result = {}
    for node2 in G.adj:
        if node2 != node1 and DFS(G, node1,node2):
            path = DFS2(G, node1, node2)
            path.pop()
            result[node2]=path.pop()
    return result

def has_cycle(G):
    visited = [False for i in G.adj]
    for node in G.adj:
        if not visited[node]:
            if has_cycle_helper(G, node, visited, node):
                return True
    return False

def has_cycle_helper(G, current, visited, parent):
    visited[current] = True
    for node in G.adj[current]:
        if not visited[node]:  
            if has_cycle_helper(G, node, visited, current): 
                return True
        elif  parent!=node: 
            return True
    return False

def is_connected(G):
    if len(G.adj) != 0:
        pDict = BFS3(G, 0)
        if(len(pDict) + 1 != len(G.adj)):
            return False
    return True
