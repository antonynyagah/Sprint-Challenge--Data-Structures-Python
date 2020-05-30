class BSTNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, name):
        
        if name < self.name:
            
            if self.left:
               
                self.left.insert(name)

            else:
                
                self.left = BSTNode(name)

       
        else:
            if self.right:
               
                self.right.insert(name)

            else:
               
                self.right = BSTNode(name)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.name == target:
            return True
        
        elif target < self.name:
            
            if self.left:               
                return self.left.contains(target)

            else:
                return False

        else:
            
            if self.right:    
                return self.right.contains(target)
            else:
                return False