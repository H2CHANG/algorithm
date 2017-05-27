'''
A well-known trick to know if an integer N is a multiple of nine is to compute the sum S of its digits.
If S is a multiple of nine, then so is N. This is a recursive test, and the depth of the recursion needed
to obtain the answer on N is called the 9-degree of N.
Your job is, given a positive number N, determine if it is a multiple of nine and, if it is, its 9-degree
'''

def total(N):
    if N % 10 == 0: return 0
    return N%10 + total(int(N/10))



def nine_degree(N,i):
    #print(N)
    sum = total(N)
    #print(sum)

    if sum == 9:
        i +=1
        print(sum,i)
        print("nine")
        return
    if sum % 9 == 0:
        i +=1
        print(sum,i)
        nine_degree(sum,i)
    else:
        print("not nine")
    #print("nine")

while(1):
    nine_degree(int(input()),0)