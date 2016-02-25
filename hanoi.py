n = int(input("input n"))

def tower(i, from_1, to, aux):
    if i == 1:
        print("move disk 1 from", from_1, "to ", to)
        return
    tower(i-1, from_1, aux, to)
    print("move disk", i, "from", from_1, "to ", to)
    tower(i-1, aux, to, from_1)

tower(n, 'A', 'C', 'B')