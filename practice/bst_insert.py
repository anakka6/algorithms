class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


a = Node(50)
insert(a, Node(30))
insert(a, Node(20))
insert(a, Node(40))
insert(a, Node(70))
insert(a, Node(60))
insert(a, Node(80))

inorder(a)
