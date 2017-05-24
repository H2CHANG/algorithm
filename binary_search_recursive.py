
def binary_search_r(s, num, front, end):
    if front > end:
        print("num isn't in array")
        return False

    middle = int((front+ end)/2)
    if num == s[middle]:
        print("num is in array")
    elif num> s[middle]:
        return binary_search_r(s, num, middle+1, end)
    else:
        return binary_search_r(s, num, front, middle-1)






s = [1,4,7,9,22,55,77,88,101,150]
binary_search_r(s,77,0,len(s)-1)