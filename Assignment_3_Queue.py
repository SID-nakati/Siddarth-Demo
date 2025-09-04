class Queue:
    def __init__(self):
        self.q = []
    def EnQ(self,val):
        self.q.append(val)

    def DQ(self):
        if len(self.q)==0 :
            print("Queue is Empty")
        else:
            print(self.q.pop(),' - Top Element Dequeued')
    def peek(self):
        if len(self.q)==0:
            print("Queue is empty")
        else:
            print(self.q[0])
    def show(self):
        for i in self.q:
            print(i)
    def size(self):
        return len(self.q)
Myq = Queue()
Myq.EnQ(2)
Myq.EnQ(42)
Myq.EnQ(23)
Myq.EnQ(74)
Myq.EnQ(8)
Myq.EnQ(5)
Myq.EnQ(7)
Myq.show()
Myq.DQ()
Myq.peek()
print("Length of Queue is ", Myq.size())