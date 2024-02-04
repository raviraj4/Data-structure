class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Queue:
    def __init__(self):
        self.head = None
        
    def enqueue(self, x):
        # if i) list empt or ii) not empty
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.ref
        else:
            print("Queue is empty")

    def display(self):
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.ref

q = Queue()
q.enqueue(0)
q.enqueue(2)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.display()
