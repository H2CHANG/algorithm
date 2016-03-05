class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def insertNode(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        elif self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tempNode = self.getLeftChild()
            tempNode.insertNode(newNode)


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def goThrough(self): #infix
        temp = self
        print(temp.getRootVal())
        if temp.getLeftChild() == None and temp.getRightChild() == None:
            return 0
        temp.getLeftChild().goThrough()
        temp.getRightChild().goThrough()

    def goThrough2(self): # Breadth-First
        Q_list = []
        Q_list.append(self)
        while len(Q_list) != 0:
            temp = Q_list.pop(0)
            print(temp.getRootVal())
            if temp.getLeftChild() != None:
                Q_list.append(temp.getLeftChild())
            if temp.getRightChild() != None:
                Q_list.append(temp.getRightChild())




r = BinaryTree('a')
r.insertNode('b')
r.insertNode('c')
r.insertNode('d')
r.insertNode('e')
r.goThrough()
r.goThrough2()