class Graph:


    class node:
        def __init__(self, vertex, weight):
            self.node = vertex
            self.weight = weight
            self.next = None

    def __init__(self, num):
        self.vertex = num
        self.vertex_list = [None] * num
        self.MST_list = []

    def addEdge(self, vertex_1, vertex_2, weight):
        if self.vertex_list[vertex_1] is None:
            self.vertex_list[vertex_1] = self.node(vertex_2, weight)
            #self.MST_list.append((vertex_1, vertex_1, weight))
        else:
            node = self.vertex_list[vertex_1]
            while node.next is not None:
                node = node.next
            node.next = self.node(vertex_2, weight)
            #self.MST_list.append((vertex_1, vertex_2, weight))
        self.MST_list.append((vertex_1, vertex_2, weight))
    def print_MST_list(self):

        for vertex_1, vertex_2, weight in self.MST_list:
            print(vertex_1, vertex_2, weight)

    #要用 disjoint set!!
    #Ｗe can also use a list to store if the vertex has been chosen
    '''
    /* 當邊的數目為頂點的數目減1時，結束迴圈 */
    while ( EdgeNum != ( VertexNum - 1 ) ) {
        /* 有一頂點不在生成樹中時 */
        if ( Visited[Pointer->Vertex1] == 0
                || Visited[Pointer->Vertex2] == 0 ) {
            printf("==>[%d,%d]",Pointer->Vertex1,Pointer->Vertex2);
            printf("(%d)",Pointer->Weight);
            Weight += Pointer->Weight;
            EdgeNum++;    /* 邊數加1 */
            Visited[Pointer->Vertex1] = 1;    /* 設為已搜尋 */
            Visited[Pointer->Vertex2] = 1;  /* 設為已搜尋  */
        }
    '''
    def MST(self):

        self.MST_list.sort(key = lambda x:x[2])
        #self.print_MST_list()
        MST = []
        #vertex_num = 0
        #print("self.vertex=", self.vertex)
        vertex = [None]  * self.vertex
        for i in range(self.vertex):
            vertex[i] = i
         #   if i ==7:
         #       print("test=", vertex[7])


        edge_num = 1
        #print("vertex[7]=", vertex[7])

        for i in self.MST_list:
            if edge_num < self.vertex:
                x,y,w = i
                print("before loop", x,y,w)
                if self.loop(x,y,vertex):
                    pass
                else:
                    if x==1 and y ==2:
                        print("vertex[x]=", vertex[x])
                        print("vertex[y]=", vertex[y])
                    self.union(x,y, vertex)
                    edge_num += 1
                    MST.append((x,y,w))

                print("start:", x, " end:", y, " weight:", w)


            else:
                break

        for x,y,w in MST:
            print(x,y,w)

    def union(self,x,y, vertex):
        vertex[self.find(x, vertex)] = self.find(y, vertex)

    def find(self, x, vertex):
        #print("x=",x)
        #print("vertex[7]", vertex[x])
        if x == vertex[x]:
            return x
        else:
            vertex[x] = self.find(vertex[x], vertex)
            return vertex[x]

    def loop(self, x,y,vertex):
        a = self.find(x, vertex)
        b = self.find(y, vertex)
        if a == b:
            return True
        else:
            return False



    def print_list(self, MST_list):
        for i, element in enumerate(MST_list):

            while element != None:
                print(i, element.node)
                element = element.next


    def DFS(self, MST_List):
        DFS_Stack = []
        DFS_presented = []
        node = None
        for i, element in enumerate(MST_List):
            if element is not None:
                print(i)
                DFS_presented.append(i)
                DFS_Stack.append(element)
                break

        while len(DFS_Stack) != 0:
            node = DFS_Stack.pop(-1)
            print(node.node, node.weight)
            if node.next is not None:
                DFS_Stack.append(node.next)

            if MST_List[node.node] is not None and node.node not in DFS_presented:
                DFS_Stack.append(MST_List[node.node])
                DFS_presented.append(node.node)


#  單用DFS 不夠, 要標記沒有走過也就是沒有連接的node



















g = Graph(9)
#print(g.vertex_list)

g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 7, 11)
g.addEdge(1, 2, 8)
g.addEdge(7, 8 ,7)
g.addEdge(7, 6 ,1)
g.addEdge(2, 8, 2)
g.addEdge(8, 6, 6)
g.addEdge(6, 5, 2)
g.addEdge(2, 5, 4)
g.addEdge(2, 3 ,7)
g.addEdge(3, 5 ,14)
g.addEdge(3, 4, 9)
g.addEdge(5, 4, 10)

#print(g.vertex_list)
#g.DFS(g.vertex_list)
#g.print_MST_list()
g.MST()
