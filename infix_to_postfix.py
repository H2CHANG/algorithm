
class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
 #   if self.is_empty():
 #     raise Empty('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
  #  if self.is_empty():
   #   raise Empty('Stack is empty')
    return self._data.pop()               # remove last item from list

def priority(op):
    if (op == '+' or op == '-'):
        return 1
    elif(op == '*' or op == '/'):
        return 2
    else:
        return 0

def inToPostfix(infix):
  postfix = ArrayStack()
  S = ArrayStack()
  for i in infix:
    if (i.isalpha()):
      postfix.push(i)
    elif (i == '('):
      S.push(i)
    elif (i == ')'):
      while(S.top() != '('):
        postfix.push(S.pop())
      S.pop()
    elif (i == '*' or i == '+' or i == '-' or i == '/'):
      if(S.is_empty()):
          S.push(i)
      else:
        while(priority(S.top()) >= priority(i)):
          postfix.push(S.pop())
        S.push(i)
  while( not S.is_empty() ):
      postfix.push(S.pop())
  L = []
  while( not postfix.is_empty()):
      L.append(postfix.pop())
  L.reverse()
  print(L)
if __name__ == '__main__':
  infix = "(a+b)*(c+d)"
  inToPostfix(infix)