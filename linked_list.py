class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    # traversal 

    def printlist(self):
        # two conditions 
        # i) linkedlist is empty (head will be none)
        if self.head is None:
            print("list is empty")
        else:
            n = self.head
            while n is not None:
                print("|",n.data,"| -->", end=" ")
                n = n.ref
            print("\n")

    #  Insertion

    def add_begin(self, data):
        newnode = Node(data)    
        newnode.ref = self.head  
        self.head = newnode

    def add_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.add_begining(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref   
            n.ref = newnode
            
    def add_after(self,data, x):
        n = self.head
        while n is not None:
            if n.data==x:
                break
            n = n.ref
        if n is None:
            print("element not present in linked list")
        else:
            newnode = Node(data)
            newnode.ref = n.ref
            n.ref = newnode
            
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref        
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # deleting nodes 

    def delete_begin(self):
        if self.head == None:
            print("list is empty nothing to delete")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head == None:
            print("list is empty nothing to delete")
        n = self.head 
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
                
    def delete_val(self, x):
        if self.head == None:
            print("list is empty nothing to delete")
            return
        if self.head.data==x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref 
        if n.ref is None:
            print("element ",x," not present in LinkedList")
        else:
            n.ref = n.ref.ref
        
    # Search
    def search(self, x):
        n = self.head
        while n is not None:
            if n.data ==x:
                print("element ",x," found at ", n)
            n = n.ref
            
    # Size
    def size(self):
        n = self.head
        i = 0
        while n is not None:
            i+=1
            n = n.ref
        print(i)
            

# examples
        
# jojo = LinkedList()
# jojo.add_begin("george joestar")
# jojo.add_after("Jonathan joestar", "george joestar")
# jojo.add_at_end("dio joestar")
# jojo.add_at_end("joseph joestar")
# jojo.add_at_end("jotaro joestar")
# jojo.add_begin("acdc")
# jojo.add_at_end("giorno")
# jojo.printlist()

nums = LinkedList()
# add
nums.add_begin(23)
nums.add_at_end(43)
nums.add_at_end(83)
nums.add_begin(38)
nums.add_after(69,23)
nums.add_before(96,23)
# print
nums.printlist()
# searching
nums.search(83)
# size
nums.size()
# del
nums.delete_end()
nums.delete_begin()
nums.delete_val(69)
print("after deleting")
# print
nums.printlist()
nums.size()

        