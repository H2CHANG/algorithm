
from python_algo.exceptions import Empty

class Deque:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 5         # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * Deque.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0
    self._back = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def last(self):
      if self.is_empty():
          raise Empty('Queue is empty')

      return self._data[self._back-1]

  def delete_first(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer


  def delete_last(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._back - 1]
    self._data[self._back - 1] = None  # help garbage collection
    if self._back - 1 < 0:
        self._back =  len(self._data) -1
    else:
        self._back = self._back - 1

    self._size -= 1
    return answer

  def add_last(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    avail = (self._back ) % len(self._data)
    self._data[avail] = e
    self._size += 1
    self._back += 1


  def add_first(self, e):
      if self._size == len(self._data):
          self._resize(2 * len(self._data))
      if self._front - 1 < 0:
          self._front = len(self._data) -1
      else:
          self._front = self._front - 1
      self._data[self._front] = e
      self._size += 1


  def print_all(self):
      if self.is_empty():
          print("no data")
      else:
          for i in range(self._size):
              print(self._data[ (self._front + i) % (len(self._data))], ' ')




  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    #walk_back = self._back
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus



    self._front = 0                         # front has been realigned
    self._back = self._front + self._size



D = Deque()
print(D._data)
D.add_last(1)
D.add_first(2)
print(D._data)
D.add_first(3)
print(D._data)
D.add_first(4)
print(D._data)
D.add_last(5)

print(D._data)
D.add_first(7)

print(D._data)
D.add_last(8)
print(D._data)
D.add_last(9)
print(D._data)
D.add_last(10)
print(D._data)
D.add_last(11)
print(D._data)
D.add_first(12)
print(D._data)

D.add_last(13)
print(D._data)


