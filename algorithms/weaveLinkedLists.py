class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        current = self.head
        if self.head:
            while current.next is not None:
                current = current.next
            current.next = element
        else:
            self.head = element

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def weaeving(self, B):
        p1 = self.head  # single increment
        current = self.head  # double increment
        while current is not None:
            p1 = p1.next
            current = current.next.next
        current = self.head
        B.append(self.head)
        Bnode = B.head
        current = current.next
        while p1.next is not None:
            Bnode.next = p1
            Bnode = Bnode.next
            p1 = p1.next
            Bnode.next = current
            Bnode = Bnode.next
            current = current.next
        Bnode.next = p1
        Bnode = Bnode.next
        Bnode.next = None
        return B


A = LinkedList()
A.append(Node(1))
A.append(Node(2))
A.append(Node(3))
A.append(Node(4))
A.append(Node(5))
A.append(Node(6))
A.append(Node(7))
A.append(Node(8))

print('A')
A.printList()
B = LinkedList()
print('Now B')
B = A.weaeving(B)
B.printList()
