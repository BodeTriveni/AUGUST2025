class Node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right= None
root = Node(1)
root.left=Node(3)
root.left.right=Node(5)
root.left.right.left=Node(7)
    