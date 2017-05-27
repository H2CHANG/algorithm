def climb_stair(n):
    prev = 1
    curr = 2
    for i in range(3,n+1):
        curr, prev = prev+ curr, curr

    print(curr)

climb_stair(5)
