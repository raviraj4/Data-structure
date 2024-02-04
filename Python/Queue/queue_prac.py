class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class Q:
    def __init__(self):
        self.head = None
        
    def enq(self, val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head 
            while n.ref is not None:
                n = n.ref
            n.ref = newnode

    def deq(self):
        if self.head is None:
            print("empty")
        else:
            self.head = self.head.ref

    def display(self):
        n = self.head
        while n is not None:
            print(f"{n.data} -->", end=" ")
            n=n.ref


q = Q()
print("\nentry gate| ",end=" ")
q.enq(12)
q.enq(14)
q.enq(19)
q.enq(21)
q.display()
q.deq()
q.deq()
q.deq()
# q.deq()
print("\nentry gate| ",end=" ")
q.display()

            