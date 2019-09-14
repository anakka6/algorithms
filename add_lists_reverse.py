'''Add 342 and 465 and print 807, The lists are set up as 2->4->3 and 5->6->4. The output should be 7->0->8.'''


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
        while current != None:
            print(current.data)
            current = current.next

    def add_two_lists(self, N1, N2):
        carry = 0
        C = Node(2)
        D = C
        while N1 is not None or N2 is not None:
            if N1 is not None and N2 is not None:
                summation = N1.data + N2.data + carry
                current_digit = summation % 10
                carry = int(summation / 10)
                print(C.data)
                C.data = current_digit
                C = C.next
                N1 = N1.next
                N2 = N2.next
            if N1 is None and N2 is not None:
                print('got here')
                summation = carry + N2.data
                current_digit = summation % 10
                C.data = current_digit
                C = C.next
                carry = int(summation / 10)
                N2 = N2.next
            elif N2 is None and N1 is not None:
                summation = carry + N1.data
                current_digit = summation % 10
                C.data = current_digit
                C = C.next
                carry = int(summation / 10)
                N1 = N1.next
        if carry is not 0:
            print('got to carry step')
            C.data = current_digit
            C = C.next
        return D


A = LinkedList()
A.append(Node(2))
A.append(Node(4))
A.append(Node(9))

print('Printing A')
A.printList()

B = LinkedList()
B.append(Node(5))
B.append(Node(6))
B.append(Node(4))
# B.append(Node(7))

print('Printing B')
B.printList()
C = LinkedList()

D = C.add_two_lists(A.head, B.head)
print('Printing C')
# C.printList()
