
class Node:
    def __init__(self, val, p = None):
        self.l = None
        self.r = None
        self.p = p
        self.v = val
        self.BF = 0
        self.right_height=0
        self.left_height=0

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
                node.l.p = node
                self._calculate_BF(node.l)
                self._reconstructure(node.l)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)
                node.r.p = node
                self._calculate_BF(node.r)
                '''
                if node.r.v == 39:
                    print(node.r.v)
                    print(node.r.v)
                    print(node.r.p.v)
                    #self._printBFT()
                '''
                self._reconstructure(node.r)
    #after insertion
    def _calculate_BF(self, node):
        while node.p is not None:
            p = node.p


            max_height = max(node.right_height, node.left_height)
            if p.l is node:
                p.left_height = max_height + 1
            if p.r is node:
                p.right_height = max_height + 1
            p.BF = p.left_height - p.right_height
            node = p

    def _reconstructure(self, node):
        #由下往上找到x, y,z(BF>1 or < -1)
        x = node
        y = x.p
        if y is None:
            return
        z = y.p

        while z is not None and abs(z.BF)<=1:
            x = y
            y = x.p
            z = y.p
        if z is None:
            return
        elif z.BF>1:
            #left left case, single right_rotate
            if y.BF >= 0 and x.BF >= 0:
                self.right_rotate(x,y,z)
                self._recalculate_BF(x,y,z)
                self._reconstructure(y)
            #left right case, left_right_rotate
            elif y.BF < 0:
                self.left_right_rotate(x,y,z)
                self._recalculate_BF(y,x,z)
                self._reconstructure(x)
        elif z.BF<1:
            #right right case, single left_rotate
            if y.BF <= 0 and x.BF <=0:
                self.left_rotate(x,y,z)
                self._recalculate_BF(x,y,z)
                self._reconstructure(y)
            #right left case, right_left_case
            elif y.BF > 0:
                ##print(x.v)
                #print(y.v)
                #print(z.v)
                self.right_left_rotate(x,y,z)
                self._recalculate_BF(y,x,z)
                self._reconstructure(x)

    def _recalculate_BF(self,x,y,z):
        if x.r is None:
            x.right_height = 0
        else:
            x.right_height = max(x.r.left_height, x.r.right_height) + 1
        if x.l is None:
            x.left_height = 0
        else:
            x.left_height = max(x.l.left_height, x.l.right_height) + 1
        x.BF = x.left_height - x.right_height
        
        if z.r is None:
            z.right_height = 0
        else:
            z.right_height = max(z.r.left_height, z.r.right_height) + 1
        if z.l is None:
            z.left_height = 0
        else:
            z.left_height = max(z.l.left_height, z.l.right_height) + 1
        z.BF = z.left_height - z.right_height

        y.left_height = max(y.l.left_height, y.l.right_height) + 1
        y.right_height = max(y.r.left_height, y.r.right_height) + 1
        y.BF = y.left_height - y.right_height
        self._calculate_BF(y)

    def right_rotate(self,x,y,z):
        y.p = z.p
        if y.p is None:
            z.p = y
            z.l = y.r
            y.r.p = z
            y.r = z
            self.root = y
            return
        if y.p.r is z:
            y.p.r = y
        elif y.p.l is z:
            y.p.l = y
        z.p = y

        z.l = y.r
        y.r.p = z
        y.r = z


    def left_rotate(self,x,y,z):
        y.p = z.p
        if y.p is None:
            z.p = y
            z.r = y.l
            if y.l is not None:
                y.l.p = z
            y.l = z
            self.root = y
            return
        if y.p.r is z:
            y.p.r = y
        elif y.p.l is z:
            y.p.l = y
        z.p = y
        z.r = y.l
        if y.l is not None:
            y.l.p = z
        y.l = z

    def left_right_rotate(self,x,y,z):
        x.p = z
        z.l = x
        y.r = x.l
        x.l.p = y
        x.l = y
        y.p = x
        self.right_rotate(y,x,z)

    def right_left_rotate(self,x,y,z):
        x.p = z
        z.r = x
        y.l = x.r
        x.r.p = y
        x.r = y
        y.p = x
        #self.printTree()
        self.left_rotate(y,x,z)
        #self.printTree()


    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        #print("root=", node.v)
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

    def _printBFT(self):
        L = []
        L.append(self.root)
        while len(L) != 0:
            node = L.pop(0)
            print(node.v, node.BF)
            if node.l != None:
                L.append(node.l)
            if node.r != None:
                L.append(node.r)
        
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
tree.add(36)
tree.add(39)

tree._printBFT()

