#!usr/bin/python2.6

A = [5,4,1,8,7,2,6,3]

def get_min_list(A):
	min = A[0]
	for i in range(len(A)):
		if A[i] < min:
			min = A[i]
	return min

def selectionSort(A):
	B= []
	for i in range(len(A)):
		x = get_min_list(A)
		#print x
		B.append(x)
		A.remove(x)
	for i in range(len(B)):
		print B[i]

selectionSort(A)
