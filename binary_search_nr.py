

def binary_search_nr(s, num):
    low = 0
    high = len(s) -1

    while low<=high:
        middle = int((low+high)/2)
        print("middle is", s[middle])
        if s[middle] == num:
            print("num is in array")
            return True
        elif s[middle] < num:
            low = middle +1
        else:
            high = middle -1

    print("num isn't in array")
    return False








s = [1,4,7,9,22,55,77,88,101,150]
binary_search_nr(s,77)
