class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
    def append(self,val):
        newnode = Node(val)
        if not self.head :
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
    def show(self):
        temp = self.head
        while temp:
            print(temp.data,end = "->")
            temp = temp.next
        print(None)
    def insert_begin(self,val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
    def rmv(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None
ll = Linked()
ll.append(2)
ll.append(56)
ll.append(42)
ll.append(276)
ll.append(24)
ll.append(98)
ll.append(10)

ll.show()

ll.insert_begin(34)
ll.show()

ll.rmv(276)
ll.show()

        