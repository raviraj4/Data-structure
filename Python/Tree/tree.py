# not complete

class BST:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_child(self,data):
        if data == self.data:
            return 
        if data < self.data:
            # we will add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
                # BST is a recursive data structure
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)


    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        # visiting base npde
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
         
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def search(self, val):
        # order of O(LOGn) which is very efficient!
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root= BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [6,3,6,98,3,7]
    number_tree = build_tree(numbers)
  
    print("inorder :\n")
    print(number_tree.inorder())

    print(number_tree.find_min())
    print(number_tree.find_max())
  


    # print(number_tree.search(489))
    # print(number_tree.find_min())