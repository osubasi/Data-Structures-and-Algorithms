# Omer Subasi

class Queue:  
  def __init__(self):
        self.stack = []
        self.idx = 0
    
  def push(self, x: int) -> None:
        self.stack.append(x)

  def pop(self) -> int:
      r = self.stack[self.idx]
      self.idx += 1
      return r

  def peek(self) -> int:
      return self.stack[self.idx]

  def empty(self) -> bool:
      for x in self.stack[self.idx:]:
          if x:
              return False
      return True
