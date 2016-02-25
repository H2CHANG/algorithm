N = 8
Matrix = [ [0 for x in range(N)] for x in range(N)]

def isSafe(x, y, Matrix):
    return x>=0 and x<N and y>=0 and y< N and Matrix[x][y] == -1


def printSolution(Matrix):
    for i in range(N):
        for j in range(N):
            print(Matrix[i][j], end="  ")
        print()

def solveKTUtil(x, y, movei, Matrix, xMove, yMove):
    if (movei == N*N):
        return True
    for i in range(N):
        next_x = x + xMove[i]
        next_y = y + yMove[i]
        if(isSafe(next_x, next_y, Matrix)):
            Matrix[next_x][next_y] = movei
            if(solveKTUtil(next_x, next_y, movei+1, Matrix, xMove, yMove)  == True):
                return True
            else:
                Matrix[next_x][next_y] = -1
    return False


def solveKT():
    for i in range(N):
        for j in range(N):
            Matrix[i][j] = -1
    xMove = [2, 1, -1, -2, -2, -1,  1,  2]
    yMove = [1, 2,  2,  1, -1, -2, -2, -1]
    Matrix[0][0] = 0
    if (solveKTUtil(0, 0, 1, Matrix, xMove, yMove) == False):
        print("Solution does not exist")
        return False
    else:
        printSolution(Matrix)

    return True



solveKT()