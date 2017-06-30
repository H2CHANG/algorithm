from python_algo import array_stack

N = 8
Matrix = [ [0 for x in range(N)] for x in range(N)]
s = array_stack.ArrayStack()
num = 0

def printSolution():
    for i in range(N):
        for j in range(N):
            print(Matrix[i][j], end="  ")
        print()
    print()


def printStack():
    for i in s.content():
        print(i)


def isSafe(x, y):
    return x>=0 and x<N and y>=0 and y< N and Matrix[x][y] == 0

def solveTest(x,y,k,xMove, yMove):
    global num

    for i in range(k,8):

        if isSafe(x+xMove[i], y+yMove[i]):
            num = num +  1
            Matrix[x][y] = num
            '''
            print("#######is Safe##########")
            print(x,y,i,num)
            printSolution()
            print("#######is Safe##########")
            '''''
            s.push((x,y,i))

            return True
    return False



def go(i,j):
    xMove = [2, 1, -1, -2, -2, -1,  1,  2]
    yMove = [1, 2,  2,  1, -1, -2, -2, -1]
    k = 0
    while True:
        global num

        if solveTest(i,j,k, xMove, yMove):
            if num == N * N -1:
                i = i + xMove[s.top()[2]]
                j = j + yMove[s.top()[2]]
                Matrix[i][j] = num + 1
                return True
            i = i + xMove[s.top()[2]]
            j = j + yMove[s.top()[2]]

            k = 0
            print("##########solvetest#########")
            printStack()
            printSolution()
            print("##########solvetest#########")
        else:
            if s.is_empty():
                return False

            i,j,k = s.pop()
            k = k +1

            Matrix[i][j]=0
            num = num -1
            print("####### else #########")
            printStack()
            print("####### esle ##########")








if go(0,0) :
    print("############solution##########")
    printSolution()
else:
    print("no solution")
