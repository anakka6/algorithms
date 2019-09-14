class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class trialLinkedList:
    def __init__(self, head):
        head = None
        self.head = head


class LinkedList:
    def __init__(self, head=None):
        self. head = head

    def append(self, element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element

    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def getPosition(self, position):
        current = self.head
        currentPosition = 1
        if currentPosition == position:
            return self.head
        else:
            while current != None:
                if currentPosition == position:
                    return current
                currentPosition += 1
                current = current.next

    def insert(self, new_element, position):
        current = self.head
        currentPosition = 1
        if position == 1:
            self.head = new_element
            new_element.next = current
        else:
            while current.next != None:
                if currentPosition == (position - 1):
                    new_element.next = current.next
                    current.next = new_element
                currentPosition += 1
                current = current.next
            if position > currentPosition:
                current.next = new_element
        return None

    def delete(self, value):
        counter = 0
        if self.head.data == value:
            self.head = self.head.next
            counter += 1
        else:
            current = self.head
            while current.next.next != None:
                if current.next.data == value:
                    current.next = current.next.next
                    counter += 1
                current = current.next
        if counter == 0:
            print('The Node with the value marked for deletion does not exist in the linked list')

    def weaeving(self, B):
        p1 = self.head
        current = self.head
        while current is not None:
            p1 = p1.next
            current = current.next.next
        current = self.head
        B.head = current
        Bcurrent = B.head
        current = current.next
        Bcurrent.next = p1
        Bcurrent = Bcurrent.next
        Bcurrent.next = current
        Bcurrent = Bcurrent.next
        Bcurrent.next = None
    return B


A = LinkedList(Node(1))
# A.printList()
A.append(Node(2))
A.append(Node(3))
A.printList()
print('After insertion')
A.insert(Node(5), 5)
A.printList()

A.delete(1)
print('After deletion')
A.printList()
# print(A.head.next.next.data)
# print(A.getPosition(3).data)
