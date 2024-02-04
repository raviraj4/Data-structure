# stack is data structure which allows us following operations: push, pop, peek, size, Isempty.
class Stack:
    def __init__(self):
        self.stack = list()
        
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
            

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
           return "NOTHING TO DELETE" 
        else:
            self.stack.pop()
            
    def peek(self):
        if self.is_empty():
            return "NOTHING TO PEEK" 
        else:
            return (self.stack[-1],"<- top")
            
    def display(self):
        for i in range(0,len(self.stack)):
            print(self.stack[i])
            
        
        
sk = Stack()
sk.push(2)
sk.push(3)
sk.push(12)
sk.push(13)
sk.push(1)
sk.display()
top = sk.peek()
print(top)

        
        
