class BT:
    class Node:

        def __init__(self,left=None, right=None, element=None):
            self.left = left
            self.right = right
            self.element = element

    def __init__(self):
        self.root = None
    def add_root(self,e):
        r = self.Node(element = e)
        self.root = r
    def add_node(self, e):
        node = self.Node(element = e)
        if self.root == None:
            self.root = node
            #self.root.left = self.Node(element  =e)
        else:
            self._add_node(self.root, node)
    def add_left_node(self,node):
        self.root.left = node
    def add_right_node(self, node):
        self.root.right = node

    # add node by sequence
    def _add_node(self, parent, node):
        if parent.left == None and parent.right == None:
            parent.left = node
        elif parent.left != None and parent.right == None:
            parent.right = node
        elif parent.left != None and parent.right != None:
            self._add_node(parent.left, node)

    def printTree_inorder(self):
        if(self.root != None):
            #print(self.root.element)
            self._printTree_inorder(self.root, depth=0)

    def _printTree_inorder(self, node, depth):
        if(node != None) and not isinstance(node, BT):
            #print(node.element)
            #print(node.left.element)

            self._printTree_inorder(node.left, depth + 1)
            #s = " " * depths
            #print(s, end='')
            print(node.element)
            #print(str(node.element) +)
            self._printTree_inorder(node.right, depth + 1)
        elif node != None and isinstance(node, BT):
            #print(node.root.element)
            self._printTree_inorder(node.root, depth+1)

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

    def printTree_postorder(self):
        self._printTree_postorder(self.root, depth = 0)

    def _printTree_postorder(self, node, depth):
        if node != None and type(node) is not BT:
            #print(str(node.element) + ' ')
            s = " " * depth *2
            print(s, end='')

            self._printTree_postorder(node.left, depth + 1)
            self._printTree_postorder(node.right, depth + 1)
            print(node.element)
        elif node != None and type(node) is BT:
            self._printTree_postorder(node.root, depth+1)

    def printBFT(self):
        L = []
        L.append(self.root)
        while len(L) != 0:
            node = L.pop(0)
            print(node.element,end=' ')
            if node.left != None:
                L.append(node.left)
            if node.right != None:
                L.append(node.right)

if __name__ == '__main__':
    T = BT()
    print(type(T))
    T.add_node(1)
    T.add_node(2)
    T.add_node(3)
    T.add_node(4)
    T.add_node(5)
    '''
    ##print inorder
    T.printTree_inorder()
    print("##########")
    ##breath-First Tree traversal
    T.printBFT()
    print()
    print("##########")
    #print_preorder
    T.printTree_preorder()
    '''
    T.printTree_postorder()
'''

polynomial euqation
binary delete leaf

'''