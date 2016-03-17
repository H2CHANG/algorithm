import copy

class Priority_queue:

    class _Item:

        __slot__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self,other):
            return self._key < other._key

    def __init__(self,k,v):
        self.pq = []
        self.pq.append(self._Item(k,v))

    def insert(self,k,v):
        temp = self._Item(k,v)
        self.pq = self.pq + [None] *1
        tempqueue = self.pq

        length = len(tempqueue) -1
        j = 0
        for i in reversed( range(length)):
            if tempqueue[i] < temp:
                tempqueue[i+1] = tempqueue[i]
                j = i
            else:
                print('i=',i)
                j = i+1
                break
        print('j=',j )
        self.pq[j] = temp

    def print_queue(self):
        for i in range(len(self.pq)):
            print('key=', self.pq[i]._key, "value=", self.pq[i]._value)



t = Priority_queue(3,"this")
t.print_queue()
t.insert(5, "test")
t.print_queue()
t.insert(9, "fhwoeh")
t.print_queue()
t.insert(10, "hrehg")
t.print_queue()
t.insert(1, "gwgw")
t.print_queue()

