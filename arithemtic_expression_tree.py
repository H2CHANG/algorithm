import infix_to_postfix, BT

infix = "3+(5+9)*2"
postfix = infix_to_postfix.inToPostfix(infix)
print(postfix)
op = infix_to_postfix.ArrayStack()
T= None
for i in postfix:
    if i.isdigit():
        op.push(i)
    else:
        rear = op.pop()
        front = op.pop()
        temp_tree = BT.BT()
        temp_tree.add_node(i)
        if T is None:
            temp_tree.add_node(front)
            temp_tree.add_node(rear)
            T = temp_tree
            #T.printTree_inorder()
            #print("###########")

        else:
            #print(front)
            if isinstance(rear, BT.BT):
                temp_tree.add_left_node(rear)
                temp_tree.add_node(front)
            #temp_tree.printTree_inorder()
                T = temp_tree
            elif isinstance(front, BT.BT):
                temp_tree.add_left_node(front)
                temp_tree.add_node(rear)
                T = temp_tree
            #T.printTree_inorder()
            #print(T.root)
            #print(T.root.left)
            #print(T.root.right)
            #print("@@@@@@@@@@@")


        op.push(T)

#print(type(T))
#print(T.root.element)
T.printTree_inorder()





