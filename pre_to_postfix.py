
def find(string):
    length =  len(string)
    if (length == 0):
        return 0
    if (string[0].isalpha()):
        return 1
    if (length < 2):
        return 0
    temp = string[1:length]
    print("find temp =", temp)
    m = find(temp)
    print("find m= ", m)
    if(m ==0 or length == m):
        return 0
    temp = string[m+1:length]
    print("find temp 2 =", temp)
    n = find(temp)
    print("find n =", n)
    if(n == 0):
        return 0
    return(m+n+1)



def convert(prefix, postfix):
    op = []

    post1 =[]
    opnd1 = []
    post2 = []
    opnd2 = []
    length = len(prefix)
    print("prefix = ", prefix)
    print("postfix = ", postfix)
    print("len = ", length)
    if (length == 1):
        if(prefix[0].isalpha()):
            postfix.append(prefix[0])
            return
        print("illegal")
        exit(0)
    op.append(prefix[0])
    temp = prefix[1:length]
    print("temp = ", temp)
    m = find(temp)
    print("m = ", m)
    temp = prefix[1+m:length]
    print("temp 2 =", temp)
    n = find(temp)
    print("n = ", n)
    if ( (op[0] != '+' and op[0] != '-' and op[0] != '*' and op[0] != '/' ) or (m == 0) or (n == 0) or  (m+n+1 != length) ):
        print("illegal prefix string")
        exit(1)
    opnd1.extend(prefix[1:1+m])
    opnd2.extend(prefix[1+m:n+1+m])
    print("opnd1 = ", opnd1)
    print("opnd2 = ", opnd2)
    convert(opnd1, post1)
    convert(opnd2, post2)
    print("post1 = ", post1)
    print("post2 = ", post2)
    #post1.append(post2).append(op)
    postfix.extend(post1)
    postfix.extend(post2)
    postfix.extend(op)
    print("postfix =", postfix)
    #return postfix

print(convert("-++A*BCD*EF", []))
