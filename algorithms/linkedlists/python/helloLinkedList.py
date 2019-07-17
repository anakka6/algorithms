#!/usr/local/bin/python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, head = None):
		self.head = head

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
		while current: # it is not current.next as if it checks that current.next --None then it wont print that node's data
			print(current.data)
			current = current.next

	def getPosition(self,position):
		currentPosition = 1
		current = self.head
		if position == currentPosition: # list has just one node
			return current
		else:
			while current != None:
				if currentPosition == position:
					return current
				currentPosition += 1
				current = current.next
			return None

	def insertANode(self, newNode, position):
		currentPosition = 1
		current = self.head
		if position == currentPosition:
			self.head = newNode
			newNode.next = current
		else:
			while currentPosition != (position-1) and current.next != None:
				current = current.next
				currentPosition += 1
			temp = current.next
			current.next = newNode
			newNode.next = temp
		return None

	def deleteFirstNodeWithValue(self,value):
		current = self.head
		if current.data == value:
			self.head = current.next
		else:
			while current.next.data != value:
				current = current.next
			current.next = current.next.next
		return None




A = LinkedList(Node(1))
#A.append(Node(1))
A.append(Node(2))
A.append(Node(3))
A.append(Node(4))

#print("Before inserting")
#A.printList()

print(A.getPosition(3).data)

# A.insertANode(Node(6),8)
# print("After inserting")
# A.printList()

# A.deleteFirstNodeWithValue(3)
# A.printList()