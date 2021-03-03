class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        y_becomes_root = False
        x = self
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            y_becomes_root = True
        elif x.is_right_child():
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        return y, y_becomes_root

    def rotate_left(self):
        y_becomes_root = False
        x = self
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            y_becomes_root = True
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        return y, y_becomes_root



class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            if node.parent.is_right_child():
                u = node.get_uncle()
                if u != None and u.is_red():
                    u.make_black()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node.is_left_child():
                        node = node.parent
                        y, y_becomes_root = node.rotate_right()
                        if y_becomes_root:
                            self.root = y
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    y, y_becomes_root = node.parent.parent.rotate_left()
                    if y_becomes_root:
                        self.root = y
            else:
                u = node.get_uncle()

                if u != None and u.is_red():
                    u.make_black()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node.is_right_child():
                        node = node.parent
                        y, y_becomes_root = node.rotate_left()
                        if y_becomes_root:
                            self.root = y
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    y, y_becomes_root = node.parent.parent.rotate_right()
                    if y_becomes_root:
                        self.root = y
        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

bst = RBTree()

bst.insert(9)
print(bst.__str__())
bst.insert(8)
print(bst.__str__())
bst.insert(7)
print(bst.__str__())
bst.insert(6)
print(bst.__str__())
bst.insert(5)
print(bst.__str__())
bst.insert(4)
print(bst.__str__())
bst.insert(3)
print(bst.__str__())
bst.insert(2)
print(bst.__str__())
bst.insert(1)
print(bst.__str__())
bst.insert(0)
print(bst.__str__())
