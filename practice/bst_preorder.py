class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self):
        return self.preorder_print(choc.root, '')[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


choc = BinaryTree(1)
choc.root.left = Node(2)
choc.root.right = Node(3)
choc.root.left.left = Node(4)
choc.root.left.right = Node(5)

print(choc.print_tree())
