class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if(self.root == None):
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)
            
    def __insert(self, node, value):
        newNode = BSTNode(value)
        if value < node.value:
            if node.left == None: 
                node.left = newNode
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None: 
                node.right = newNode
                node.right.parent = node
            else:
                self.__insert(node.right, value)

    
    def get_height(self):
        if self.root == None:
            return 0
        return self.__get_height(self.root)


    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))



        
            
