


def step(n):
    print(n)
    if n <=1:
        return 0
    if n %2 == 0:
        n = n/2
    else:
        n = n*3+1

    return 1 + step(n)


print(step(10))