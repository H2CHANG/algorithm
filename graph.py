class Graph:

    class Vertex:
        def __init__(self,v):
            self.name = v
            self.al = None
    class Adjacent_list:
        def __init__(self,adjacence):
            self.adjacent_node  = adjacence
            self.next = None

    def __init__(self, vertex_list = None):
        if vertex_list is None:
            vertex_list = []
        self.vertex = vertex_list

    def add(self,vertex_1, vertex_2):
        vertex_flag = False
        for i in self.vertex:
            if i.name == vertex_1:
                vertex_flag = True
                node = i.al
                while node.next is not None:
                    node = node.next
                node.next = self.Adjacent_list(vertex_2)
        if vertex_flag is False:
            v = self.Vertex(vertex_1)
            v.al = self.Adjacent_list(vertex_2)
            self.vertex.append(v)

    def goThrough(self):
        for i in self.vertex:
            print("i.name = ", i.name, "-->>", end=' ')
            node = i.al
            while node:
                print(node.adjacent_node, end=' ')
                node = node.next
            print()

    def DFS(self,start,passed = None):
        node = None
        node_pre = None
        if passed is None:
            passed = []
        if start in passed:
            return
        else:
            passed.append(start)
            #print(passed)
        for i in self.vertex:
            if i.name == start:
                node = i.al


        while node is not None:
            self.DFS(node.adjacent_node,passed)
            node = node.next
        #return passed





G = Graph()
G.add(0,1)
G.add(0,4)
G.add(1,2)
G.add(1,3)
G.add(1,4)
G.add(2,3)
G.add(3,4)

#G.goThrough()
#DFS
#print(G.DFS(0))
s = []
G.DFS(0,s)
print(s)
#################






