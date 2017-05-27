#permutation


def calculate(num):

    if num == 1 or num == 0: return 1
    return num * calculate(num-1)

def divide_ten(num):
    print("num=", num)
    if num%10 != 0: return num%10

    return divide_ten(num/10)

def permutation(N,M):
    n = calculate(N)
    print(n)
    m = calculate(N-M)
    num = int(n/m)

    print(divide_ten(num))

permutation(10,10)
