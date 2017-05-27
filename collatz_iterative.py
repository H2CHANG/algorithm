'''
def step(n):
    i = 1
    while(i>0):
        print(n)
        if n >1:
            if n %2 == 0:
                n = n/2
            else:
                n = n *3 +1
        else:
            break

        i = i +1
    return i
'''


def step(n):
    print(n)
    if n <=1:
        return 
    if n %2 == 0:
        n = n/2
    else:
        n = n*3+1

    step(n)


print(step(10))

