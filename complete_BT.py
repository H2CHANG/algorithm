#complete BT

import math

class BT:

    #Height = 0
    class Node:

        def __init__(self,left=None, right=None, element=None):
            self.left = left
            self.right = right
            self.element = element
            self.left_count = 0
            self.right_count = 0
            self.father = None


    def __init__(self):
        self.root = None
    def add_root(self,e):
        r = self.Node(element = e)
        self.root = r
    def add_node(self, e):
        node = self.Node(element = e)
        if self.root == None:
            self.root = node
            #self.Height = self.findHeight(self.root)

            #self.root.left = self.Node(element  =e)
        else:
            #self.Height = self.findHeight(self.root)

            self._add_node(self.root, node)
            self._upheap(node)

    def _upheap(self, node):
        while node.father is not None:
            if node.father.element < node.element:
                break
            else:
                temp = node.father.element
                node.father.element = node.element
                node.element = temp
                node = node.father


    def findHeight(self, node):
        if node is None:
            return -1
        return 1+ max(self.findHeight(node.left), self.findHeight(node.right))


    # add node by height
    def _add_node(self, parent, node):

        h = self.findHeight(parent)
        '''
        if node.element == 7:
            print("%%%%")
            print("h=",h)
            print(int(math.pow(2,h)-1))
            print(parent.left_count)
            print(parent.right_count)
        '''
        if parent.left_count < int(math.pow(2,h)-1):

            if parent.left is None:
                parent.left = node
                node.father = parent
                parent.left_count += 1
                self.parent_count(parent)
            else:
                self._add_node(parent.left, node)
        elif parent.left_count == int(math.pow(2,h)-1) and parent.right_count < int(math.pow(2,h)-1):

            if parent.right is None:
                parent.right = node
                node.father = parent
                parent.right_count += 1
                self.parent_count(parent)
            else:
                self._add_node(parent.right, node)

        elif parent.left_count == int(math.pow(2,h)-1) and parent.right_count == int(math.pow(2,h)-1):

            if parent.left is None:
                parent.left = node
                node.father = parent
                parent.left_count += 1
                self.parent_count(parent)
            else:
                self._add_node(parent.left, node)





    def parent_count(self, child):
        while child.father is not None:
            if child.father.left == child:
                # must make parent count = 0
                child.father.left_count = 0
                child.father.left_count += child.left_count + child.right_count + 1
            else:
                child.father.right_count = 0
                child.father.right_count += child.left_count + child.right_count + 1

            child = child.father


    def printTree_preorder(self):
        self._printTree_preorder(self.root, depth = 0)

    def _printTree_preorder(self, node, depth):
        if node != None:
            #print(str(node.element) + ' ')
            s = " " * depth *2
            print(s, end='')
            print(node.element)
            self._printTree_preorder(node.left, depth + 1)
            self._printTree_preorder(node.right, depth + 1)

    def remove_min(self):
        min = self.root
        last = self._last_node()
        self.root.element = last.element
        if last.father.left is last:
            last.father.left = None
        elif last.father.right is last:
            last.father.right = None
        self._downheap(self.root)

    def _downheap(self, node):
        
        # if left or right of node exist
        while node.left is not None or node.right is not None:
            if node.left is not None and node.right is None:
                if node.element < node.left.element:
                    break
                else:
                    temp = node.left.element
                    node.left.element = node.element
                    node.element = temp
                    node = node.left
            elif node.left is not None and node.right is not None:
                if node.element < node.left.element and node.element < node.right.element:
                    break
                elif node.left.element > node.right.element:
                    temp = node.right.element
                    node.right.element = node.element
                    node.element = temp
                    node = node.right
                elif node.left.element < node.right.element:
                    temp = node.left.element
                    node.left.element = node.element
                    node.element = temp
                    node = node.left
            elif node.left is None and node.right is not None:
                if node.element < node.right.element:
                    break
                else:
                    temp = node.right.element
                    node.right.element = node.element
                    node.element = temp
                    node = node.right



    #return last node by BFT
    def _last_node(self):

        L = []
        t = []
        L.append(self.root)
        while len(L) != 0:
            node = L.pop(0)
            t.append(node)
            print(node.element,end=' ')
            if node.left != None:
                L.append(node.left)
            if node.right != None:
                L.append(node.right)
        #print("t = ", t)
        #print("t=[-1]", t[-1])
        return t[-1]

if __name__ == '__main__':
    T = BT()
    #print(type(T))
    T.add_node(7)

    T.add_node(11)

    T.add_node(12)
    #print(T.findHeight(T.root))
    T.add_node(13)
    T.add_node(14)
    T.add_node(15)
    T.add_node(16)

    #print(T.findHeight(T.root))
    #T.printTree_preorder()

    T.add_node(17)
    T.add_node(18)
    T.add_node(19)
    T.add_node(20)
    T.add_node(21)
    T.add_node(22)
    T.add_node(1)
    T.add_node(8)
    print(T.findHeight(T.root))
    T.printTree_preorder()
    #T.add_node(8)
    #print(T.findHeight(T.root))
    #T.printTree_preorder()
    T.remove_min()
    print(T.findHeight(T.root))
    T.printTree_preorder()
    T._last_node()

