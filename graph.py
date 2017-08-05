class Graph:
    #class variable for loop detection
    loop = False

    class Vertex:
        def __init__(self,v):
            self.name = v
            self.al = None
    class Adjacent_list:
        def __init__(self,adjacence):
            self.adjacent_node  = adjacence
            self.next = None
    class loop_edege:
        def __init__(self, head):
            self.head = head
            self.w = None

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
        # for loop detect
        #recList = []
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

    def BFS(self, start):
        q = []
        compare_list = [0,0,0,0,0,]
        node = None
        q.append(start)
        while len(q) != 0:
            temp = q.pop(0)
            print("temp = ",temp,end=' ')
            for i in self.vertex:
                if i.name == temp:
                    node = i.al
            while node is not None and compare_list[node.adjacent_node] == 0:
                q.append(node.adjacent_node)
                compare_list[node.adjacent_node] = 1
                node = node.next

    #detect loop by DFS implemented by stack/List, by recArray, return if any vertex in recArray
    def loop(self, start):
        DFS_vertex = []
        DFS_Stack = []
        vertex = []
        recList = []
        node = None
        next_node = None
        name = None
        for i in self.vertex:
            if i.name == start:
                node = i
                vertex.append(node.name)
                break
        #DFS_vertex.append(node)
        print(node.name)
        DFS_Stack.append([node.name,node.al])
        while len(DFS_Stack) != 0:
            (pre_name, node) = DFS_Stack.pop(-1)

            if node.next is not None:
                DFS_Stack.append([node.adjacent_node,node.next])
            flag = False
            for i in self.vertex:
                 # node not in self.vertex
                if i.name == node.adjacent_node:
                    flag = True
                    name = i.name
                    if i.name not in vertex:
                        next_node = i
                        print(next_node.name)
                        vertex.append(next_node.name)
                        DFS_Stack.append([next_node.name, next_node.al])

                        break
                    else:
                        recList.append([name, node.adjacent_node])

            if flag is False:
                if node.adjacent_node not in vertex:
                    print(node.adjacent_node)
                    vertex.append(node.adjacent_node)
                else:
                    recList.append([name, node.adjacent_node])
        for i in recList:
            print(i)
        if len(recList) != 0:
            print("The graph is a loop graph")
        else:
            print("The graph is not a loop graph")








G = Graph()
G.add(0,1)
G.add(0,4)
G.add(1,2)
G.add(1,3)
#G.add(1,4)
#G.add(2,3)
G.add(3,4)

#G.goThrough()
#DFS
#print(G.DFS(0))
#s = []
#G.DFS(0,s)
#print(s)
#DFS by Stack
G.loop(0)
#################
#BFS
#G.BFS(0)







