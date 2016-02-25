N = 8
Matrix = [ [0 for x in range(N)] for x in range(N)]
test_Matrix = [ [0 for x in range(N)] for x in range(N)]

def isSafe(x, y, Matrix):
   # print("this is is safe")
   # print("x,y= ", x, y)

    if Matrix[x][y] != -1:
        return False
    else:
        for i in range(N):
            for j in range(N):
                if Matrix[i][j] != -1:
    #                print("i,j = ",i,j)
                    if i == x or j == y or (x-i)/(y-j) == 1 or (x-i)/(y-j) == -1:
                        return False
    #printSolution(Matrix)
    #print("This is OK")
    return True


def printSolution(Matrix):
    for i in range(N):
        for j in range(N):
            print(Matrix[i][j], end="  ")
        print()

def solveKTUtil(x, y, movei, Matrix):
    if (movei == N):
        return True
    for i in range(N):
        for j in range(N):
            if i == 0 and j ==0:
                continue
            next_x, next_y = test_Matrix[i][j]
            if(isSafe(next_x, next_y, Matrix)):
            #    print(next_x, next_y, movei)
                Matrix[next_x][next_y] = movei
            #    printSolution(Matrix)
                if(solveKTUtil(next_x, next_y, movei+1, Matrix)  == True):
                    return True
                else:
                    Matrix[next_x][next_y] = -1
    return False


def solveQueen():
    for i in range(N):
        for j in range(N):
            Matrix[i][j] = -1
            test_Matrix[i][j] = (i,j)
    Matrix[0][0] = 0
    printSolution(Matrix)
    if (solveKTUtil(0, 0, 1, Matrix) == False):
        print("Solution does not exist")
        return False
    else:
        printSolution(Matrix)

    return True



solveQueen()