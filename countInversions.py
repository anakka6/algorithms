#!/usr/bin/python2.6

with open('/home/anakka/Desktop/Algorithms/num.txt','r') as file:
	A = file.readlines()

#for i in range(len(A)):
#	A[i] = int(A[i])

def MergeAndCountSplitInversions(C,D):
	n = len(C) + len(D)
	B = [0 for x in range(n)]
	i= 0
	j = 0
	splitInv = 0
	for k in range(n):
		if i <len(C) and j < len(D):
			if (int(C[i]) > int(D[j])):
			    if (C[i] <= D[j]):
				    print C[i], D[j]
				    print len(C[i]), len(D[j])
				    exit(0)
			
			if C[i] < D[j]:
				B[k] = C[i]
				i = i+1
			else:
				B[k] = D[j]
				j = j+1
				splitInv = splitInv +(len(C)-i)
		elif i>= len(C):
			B[k] = D[j]
			j = j+1
		elif j>= len(D):
			B[k] = C[i]
			i=i+1
	return B,splitInv

def sortAndCountInversions(A):
	n = len(A)
	if n == 0 or n == 1:
		return (A,0)
	else:
		B = [0 for x in range(n)]
		if n%2 ==0:
			A1 = [0 for x in range(len(A)/2)]
			A2 = [0 for x in range(len(A)/2)]
			C = [0 for x in range(len(A)/2)]
			D = [0 for x in range(len(A)/2)]
			for i in range(len(A)/2):
				A1[i] = A[i]
				A2[i] = A[i+len(A)/2]
		else:
			A1 = [0 for x in range(n/2)]
			A2 = [0 for x in range(n - (n/2))]
			C = [0 for x in range(n/2)]
			D = [0 for x in range(n  - (n/2))]
			for i in range(n/2):
				A1[i] = A[i]
				A2[i] = A[i+len(A)/2]
			A2[i+1] = A[n-1]
		C,leftInv = sortAndCountInversions(A1)
		D,rightInv = sortAndCountInversions(A2)
		B, splitInv = MergeAndCountSplitInversions(C,D)
		return (B,(leftInv+rightInv+splitInv))


X,y = sortAndCountInversions(A)
print "Inversions from MergeSort:",y

def bruteForce(A):
	n = len(A)
	numInv = 0
	for i in range(n-1):
		for j in range(i+1,n):
			if A[i] > A[j]:
				numInv = numInv +1
	return numInv
