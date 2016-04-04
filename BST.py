
class Node:
    def __init__(self, val, p = None):
        self.l = None
        self.r = None
        self.p = p
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            return self._find(val, node.l)
        elif(val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def _find_1(self, val, node, parent = None):

        if(val == node.v):
            #print("get it !!!!!!!")
            #print('val_1 = ', val)
            #print(node)
            #print(parent)
            return (node, parent)

        elif(val < node.v and node.l != None):
            return self._find_1(val, node.l, node)
        elif(val > node.v and node.r != None):
            return self._find_1(val, node.r, node)


    # del node in BST
    def deleteNode(self, val):
        node = None
        parent = None
        ret_val = None
        print('val = ', val)
        if(self.root != None):
            ret_val_1 = self._find_1(val, self.root)
            #print('mgwognwo',ret_val_1)
            node = ret_val_1[0]
            parent = ret_val_1[1]
            #int('test', node.v)
            #print('test', parent.v)
            if node != None:

                if node.l == None and node.r == None:
                    if node is parent.l:
                        parent.l = None
                        node = None
                    else:
                        parent.r = None
                        del node
                elif (node.l == None and node.r != None):
                    if node is parent.r:
                        parent.r = node.r
                        del node
                    else:
                        parent.l = node.r
                        del node
                elif (node.l != None and node.r == None):
                    if node is parent.l:
                        parent.l = node.l
                        del node
                    else:
                        parent.r = node.l
                        del node
                else:
                    val_node = node
                    parent = node
                    node = node.r
                    while node.l != None:
                        parent = node
                        node = node.l
                    val_node.v = node.v
                    parent.l = None
                    del node


    def is_root(self, node):
       if self.root is node:
           return True
       else:
           return False


            
    def depth(self, val):
       node, parent = self._find_1(val, self.root)
       if self.is_root(node):
           return 0
       else:
           return 1 + self.depth(parent.v)

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

    def rotate(self, val):
        node = None
        parent = None

        if(self.root != None):
            ret_val_1 = self._find_1(val, self.root)

            node = ret_val_1[0]
            parent = ret_val_1[1]

            # right rotate
            if parent.l is node:
                if node.r != None:
                    parent.l = node.r
                else:
                    parent.l = None
                node.r = parent
            #left rotate
            else:
                if node.l != None:
                    parent.r = node.l
                else:
                    parent.r = None
                node.l = parent
            self.root = node


    def goThrough2(self): # Breadth-First
        Q_list = []
        Q_list.append(self.root)
        while len(Q_list) != 0:
            temp = Q_list.pop(0)
            print(temp.v)
            if temp.l != None:
                Q_list.append(temp.l)
            if temp.r != None:
                Q_list.append(temp.r)

    # add Height
    def is_leaf(self, node):
        #print("if leaf")
        #print(node.v)
        if node.l == None and node.r == None:
            return True
        else:
            return False

    def children(self, node):
        return (node.l, node.r)

    def _height(self, node):

        if self.is_leaf(node):
            ##print("leaf")
            #print(node.v)
            return 0
        else:
            #print("not leaf")
            #print(node.v)
            return 1 + max(self._height(c) for c in self.children(node) if c != None)


    def height(self, val):
        node, parent = self._find_1(val, self.root)
        #print("nodenodnoenohfoe")
        #print(node)
        return self._height(node)

tree = Tree()
tree.add(28)
tree.add(15)
tree.add(40)
tree.add(10)
tree.add(16)
tree.add(30)
tree.add(50)
tree.add(29)
tree.add(35)
tree.add(41)
tree.add(51)

tree.printTree()
print("!!!!!!!!!!!!!!")
print( tree.height(28))
print("delete node")
tree.deleteNode(28)
tree.printTree()
print("!!!!!!!!!!!!!!")
print( tree.height(29))


print("################")
tree.rotate(40)
tree.printTree()

print("$$$$$$$$$$$$$")
tree.goThrough2()


print("%%%%%%%%%%%%%%%")
print( tree.depth(51) )

print("################")
tree.rotate(29)
tree.printTree()


print("$$$$$$$$$$$$$")
tree.goThrough2()


print("%%%%%%%%%%%%%%%")
print( tree.depth(51) )


print("!!!!!!!!!!!!!!")
print( tree.height(40))

