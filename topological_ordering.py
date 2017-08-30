# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def incoming_number(self, incoming_list):
        for i in range(self.V):
            for j in self.graph[i]:
                incoming_list[j] += 1





g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

incoming_list = [0] * g.V
g.incoming_number(incoming_list)
active_list = [ i for i,j in enumerate(incoming_list) if j == 0]
print(active_list)
print(incoming_list)
used_list = []
while len(active_list) != 0:
    v = active_list.pop(0)
    print(v)
    used_list.append(v)
    for i in g.graph[v]:
        incoming_list[i] -= 1
        if incoming_list[i] == 0:
            active_list.append(i)

    g.graph[v] = []


