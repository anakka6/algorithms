#!/usr/local/bin/python3


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, head):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # watch out if you are adding a new node or just the data to be added is
    # passed in the function
    def insertFirst(self, new_element):
        temp = self.head
        self.head = new_element
        new_element.next = temp

    def delete_first(self):
        self.head = self.head.next


class Stack(object):

    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insertFirst(new_element)

    def printStack(self):
        self.ll.printList()

    def pop(self):
        popped_element = self.ll.head
        self.ll.delete_first()
        return popped_element


# A = LinkedList(Node(1))
# A.append(Node(2))
# A.append(Node(3))
# A.printList()
# print("After inserting")
# A.insertFirst(Node(4))
# A.printList()
# print("Delete first")
# A.delete_first()
# A.printList()

B = Stack(Node(1))
B.push(Node(2))
B.push(Node(3))
print("Added elements to Stack")
B.printStack()
print("Popping")
print(B.pop().data)
print("Printing Stack")
B.printStack()
