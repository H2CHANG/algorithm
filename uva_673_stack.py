from python_algo import array_stack

s1 = "(([()])))"
s2 = "([()[]()])()"


def check_T(s):
    check_list = {
        '(':')',
        '[':']'
    }
    C = array_stack.ArrayStack()
    for i in s:
        if i in '([':
            C.push(i)
            print(C.content())
        else:
            if (C.is_empty()):
                print("False")
                return
            elif (check_list[C.top()] == i):
                C.pop()
                print(C.content())
    #print(C.content())
    if C.is_empty():
        print("True")
    else:
        print("False")



check_T(s1)
check_T(s2)