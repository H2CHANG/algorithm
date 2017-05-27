
def add_function(n):
    if n == 0: return 0
    if n %10 > 0: return n%10
    return add_function(n/10)


while(1):
    sum = 0
    p, q = input().split()
    p = int(p)
    q = int(q)
    if p <0 and q <0: exit()
    for i in range(p, q+1):
        sum = sum + add_function(i)
    print(int(sum))

