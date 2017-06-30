from python_algo import circular_queue

class J_circular_queue(circular_queue.CircularQueue):
    def dequeue(self):

        if self.is_empty():
          raise Empty('Queue is empty')
        #head = self._tail._next
        if self._size == 1:                   # removing only element
          self._tail = None                   # queue becomes empty
        else:
            self._head = self._head._next
            remove_node = self._head._next
            if remove_node is self._tail:
                self._tail = self._head
            self._head._next = remove_node._next
            self._head = self._head._next

          #self._tail._next = head._next._next    # bypass the old head
        self._size -= 1

        return remove_node._element
    def print_queue(self):

        for i in range(len(self)):

            print(self._head._element)
            self._head = self._head._next


cq_Joseph = J_circular_queue()

for i in range(1,42):
    cq_Joseph.enqueue(i)
cq_Joseph.first()
print(cq_Joseph._head)
print(cq_Joseph._tail)
print(cq_Joseph._tail._next)
#cq_Joseph.print_queue()


while len(cq_Joseph) > 2:
    print(cq_Joseph.dequeue())
    #cq_Joseph.print_queue()
    #print("##############")
    #print(cq_Joseph._head._element)
    #print("****************")

cq_Joseph.print_queue()
print(cq_Joseph._tail._element)














