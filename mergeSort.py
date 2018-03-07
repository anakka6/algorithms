#!/usr/bin/python2.6

A = [5,4,1,8,7,2,6,3]


def mergeSort(A):
	if len(A) == 1:
		return A
	else:
		B = [ 0 for x in range(len(A))]
		A1 = [0 for x in range(len(A)/2)]
		A2 = [0 for x in range(len(A)/2)]
		for i in range(len(A)/2):
			A1[i] = A[i]
			A2[i] = A[i+len(A)/2]
		A1 = mergeSort(A1)
		A2 = mergeSort(A2)
		i=0
		j=0
		Merge_size = len(A1)+len(A2)
		for k in range(Merge_size):
			if i< len(A1)and j < len(A2):
				if A1[i] < A2[j]:
					B[k] = A1[i]
					i = i+1
				else:
					B[k] = A2[j]
					j = j+1
			elif i >= len(A1):
				B[k] = A2[j]
				j = j+1
			elif j >= len(A2):
				B[k] = A1[i]
				i = i+1
		return B

B = mergeSort(A)

for k in range(len(B)):
	print B[k]
