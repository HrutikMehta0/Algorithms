# Define Node
class Node():
    def __init__(self, time, val):
        self.time = time
        self.greatest = val
        self.val = val  # Value of Node
        self.parent = None  # Parent of Node
        self.left = None  # Left Child of Node
        self.right = None  # Right Child of Node
        self.color = 1  # Red Node as new node is always inserted as Red Node


# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = Node(0, 0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        self.insertNode(0, 0)

    def update(self, t1, value):
        self.insertNode(t1, value)

    def Greatest(self, t1, t2):
        maxLength = 0
        node = self.root
        while node is not None and t1 < node.time or t2 > node.time:
            if t1 > node.time:
                if node.time == t1:
                    maxLength = max(maxLength, node.val)
                else:
                    if maxLength == 0:
                        maxLength = node.val
                    if node.right.parent is not None and t1 > node.right.time:
                        maxLength = 0
                    else:
                        maxLength = max(maxLength, node.val)
                if node.right.parent is not None:
                    node = node.right
                else:
                    node = None
            elif node.left is not None:
                if node.time == t2:
                    maxLength = max(maxLength, node.val)
                else:
                    if maxLength == 0:
                        maxLength = node.val
                    if node.left.parent is not None and t1 <= node.left.val:
                        maxLength = 0
                    else:
                        maxLength = max(maxLength, node.val)
                if node.left.parent is not None:
                    node = node.left
                else:
                    node = None

    # Insert New Node
    def insertNode(self, time, value):
        node = Node(time, value)
        node.parent = None
        node.val = value
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # Set root colour as Red
        node.greatest = value

        y = None
        x = self.root
        if self.root is not None and self.root.greatest < value:
            self.root.greatest = value

        while x != self.NULL:  # Find position for new node
            y = x
            if node.time < x.time:
                x = x.left
            else:
                x = x.right

        node.parent = y  # Set parent of Node as y
        if y == None:  # If parent i.e, is none then it is root node
            self.root = node
            self.root.greatest = node.greatest
        elif node.time < y.time:  # Check if it is right Node or Left Node by checking the value
            y.left = node
            y.greatest = max(node.greatest, y.greatest)
        else:
            y.right = node
            y.greatest = max(node.greatest, y.greatest)

        if node.parent == None:  # Root node is always Black
            node.color = 0
            return

        if node.parent.parent == None:  # If parent of node is Root Node
            return

        self.fixInsert(node)  # Else call for Fix Up

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    # Code for left rotate
    def LR(self, x):
        y = x.right  # Y = Right child of x
        x.right = y.left  # Change right child of x to left child of y
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent  # Change parent of y as parent of x
        y.greatest = x.greatest
        if x.parent == None:  # If parent of x == None ie. root node
            self.root = y  # Set y as root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Code for right rotate
    def RR(self, x):
        y = x.left  # Y = Left child of x
        x.left = y.right  # Change left child of x to right child of y
        x.greatest = y.greatest
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent  # Change parent of y as parent of x
        if x.parent == None:  # If x is root node
            self.root = y  # Set y as root
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix Up Insertion
    def fixInsert(self, k):
        while k.parent.color == 1:  # While parent is red
            if k.parent == k.parent.parent.right:  # if parent is right child of its parent
                u = k.parent.parent.left  # Left child of grandparent
                if u.color == 1:  # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0  # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # Set grandparent node as Red
                    k = k.parent.parent  # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:  # If k is left child of it's parent
                        k = k.parent
                        self.RR(k)  # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:  # if parent is left child of its parent
                u = k.parent.parent.right  # Right child of grandparent
                if u.color == 1:  # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0  # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # set color of grandparent as Red
                    k = k.parent.parent  # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:  # if k is right child of its parent
                        k = k.parent
                        self.LR(k)  # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)  # Call right rotate on grandparent
            if k == self.root:  # If k reaches root then break
                break
        self.root.color = 0  # Set color of root as black


if __name__ == "__main__":
    bst = RBTree()

    bst.update(2, 1)
    bst.update(3, 12)
    bst.update(5, 17)
    #print(bst.Greatest(6, 6))
    #print(bst.Greatest(5, 6))
    bst.update(8, 9)
    #print(bst.Greatest(6, 11))
    #print(bst.Greatest(0, 2))
    bst.update(15, 9)
    bst.update(17, 2)
    bst.update(18, 20)
    print('Hello')
    #print(bst.Greatest(2, 19))
