'''

def climb_stair(n):
    prev = 1
    curr = 2
    for i in range(3,n+1):
        curr, prev = prev+ curr, curr

    print(curr)
'''



def climb_stair(n):
    if n == 1: return 1
    if n == 2: return 2
    return climb_stair(n-1) + climb_stair(n-2)


print(climb_stair(5))