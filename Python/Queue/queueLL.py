class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Queue:
    def __init__(self):
        self.head = None
        
    def enqueue(self, data):
        newnode = Node(data)
        newnode.ref = self.head
        self.head = newnode

    def dequeue(self):

        if self.head is None:
            print("empty")
            return
        n = self.head
        try:
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
        except AttributeError:
            while n is not None:
                n = n.ref
            n = None
            print("list ended")
        
        
        

    def peek(self):
        n = self.head
        while n.ref is not None:
            n = n.ref
        print(n.data,"<--top")
        
        
    def display(self):
        n = self.head
        while n is not None:
            print(n.data,)
            n = n.ref


q = Queue()
q.enqueue(0)
q.enqueue(2)
q.enqueue(4)
q.enqueue(5)
q.enqueue(7)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

q.display()
print("\n----ticket counter---")
q.peek()
        
        
        
        