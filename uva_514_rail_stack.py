'''
    運用兩個queue or array, 來存放 Ｂ車站也就是結果, 另一個存放 Ａ車站也就是1,2,3,4,5...出發順序
    中間車站用stack 來存
    Algorithm:
    每個A車站的車依序存到stack中
    但只要stack中的top跟 Ｂ車站的front 是相同的, 那就pop stack and queue, 這樣表示車頭到 B 車站也就是目的地去了

'''

N = int(input("幾台火車"))
A = []
#B = []
B = [ int(i) for i in input("結果").split()]
C = []
print("B=", B)
for i in range(N):
    A.append(i+1)
print("A=", A)
for i in A:
    C.append(i)
    print("C=",C)
    while(len(C)!=0 and C[-1] == B[0]):
        C.pop()
        B.pop(0)
        print("C=",C)
        print("B=",B)

if len(C) == 0:
    print("True")
else:
    print("False")

