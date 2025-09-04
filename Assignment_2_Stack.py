class Stack:
  def __init__(self):
    self.stack = []
 
  def push(self, element):
    self.stack.append(element)
 
  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()
 
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]
 
  def isEmpty(self):
    return len(self.stack) == 0
  def show(self):
    for i in self.stack :
      print(i)
 
  def size(self):
    return len(self.stack)
MyStack = Stack()
MyStack.push(1)
MyStack.push(3)
MyStack.push(4)
MyStack.push(13)
MyStack.push(6)
MyStack.push(18)
MyStack.show()
MyStack.pop()
print("Top Element is ",MyStack.peek())
