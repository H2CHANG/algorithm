Matrix = [ [0 for x in range(8)] for x in range(8)]


startx = int(input("startx = "))
starty = int(input("starty = "))

def travel(x, y):
    ktmovex = [-2,-1,1,2,2,1,-1,-2]
    ktmovey = [1,2,2,1,-1,-2,-2,-1]
    nextx = [0,0,0,0,0,0,0,0]
    nexty = [0,0,0,0,0,0,0,0]
    exists = [0,0,0,0,0,0,0,0]
    i = j = L = tmpx = tmpy = count = min = tmp = 0
    i = x
    j = y
    Matrix[x][y]=1
    for m in range(2, 65): # next
        for L in range(8): # record direction
            exists[L] = 0
            nextx[L] = 0
            nexty[L] = 0
        L = 0
        for k in range(8):
            tmpx = i + ktmovex[k]
            tmpy = j + ktmovey[k]
            if (tmpx<0 or tmpx > 7 or tmpy < 0  or tmpy > 7):
                continue
            if (Matrix[tmpx][tmpy] == 0):
                nextx[L] = tmpx
                nexty[L] = tmpy
                L += 1
        count = L
        if(count == 0):
            return 0
        elif(count == 1):
            min = 0
        else:
            for L in range(count):
                for k in range(8):
                    tmpx = nextx[L] + ktmovex[k]
                    tmpy = nexty[L] + ktmovey[k]
                    if (tmpx<0 or tmpx > 7 or tmpy < 0  or tmpy > 7):
                        continue
                    if (Matrix[tmpx][tmpy] == 0):
                        exists[L] += 1
            tmp = exists[0]
            min = 0
            for L in range(1,count):
                if(exists[L] < tmp):
                    tmp = exists[L]
                    min = L
        i = nextx[min]
        j = nexty[min]
        Matrix[i][j] = m
    return 1





if (travel(startx, starty)):
    print("travel OK")
else:
    print("travel failure")

for i in range(8):
    for j in range(8):
        print(Matrix[i][j], end="  ")
    print("\n")
