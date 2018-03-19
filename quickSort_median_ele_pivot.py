#!usr/bin/python2.6

#A = [5,4,1,8,7,2,6,10,3,9]
with open('/home/anakka/Desktop/Algorithms/QuickSort.txt','r') as file:
	A = file.readlines()

for i in range(len(A)):
	A[i] = int(A[i])

def swap(A,a,b):
	k = A[b]
	A[b] = A[a]
	A[a] = k
	return A

def printArray(A):
	for i in range(len(A)):
		print A[i]

def partition(A,l,r):
	p = A[l]
	i = l+1
	for j in range(i,r+1):
		if A[j] < p:
			A = swap(A,i,j)
			i = i+1
	A = swap(A,l,i-1)
	return i-1 # final pivot position

def choosePivot(A,l,r):
	a = l
	c = r
	b = (l+r)/2
	if (A[a] <A[c] and A[c]<A[b]) or (A[b]<A[c] and A[c] < A[a]):
		pivotPosition = c
	elif (A[a] <A[b] and A[b]<A[c]) or (A[c]<A[b] and A[b] < A[a]):
		pivotPosition = b
	else:
		pivotPosition = a
	return pivotPosition

# x = choosePivot(A,12,20)
# print x


def quickSort(A,l,r):
	comparisons = 0
	if l >= r:
		return A,0
	else:
		i = choosePivot(A,l,r)
		A = swap(A,l,i)
		j = partition(A,l,r)
		comparisons = comparisons + (r-l)
		#print "quickSort(A,",l,",",j-1,")"
		A,func_comparisons_left = quickSort(A,l,j-1)
		#print "quickSort(A,",j+1,",",r,")"
		A,func_comparisons_right = quickSort(A,j+1,r)
		comparisons = comparisons + func_comparisons_right +func_comparisons_left
	return A,comparisons


A,comparisons = quickSort(A,0,len(A)-1)

print "Final result"
#printArray(A)

print "comparisons:",comparisons

for i in range(len(A)-1):
	if(A[i] >A[i+1]):
		print "Oops!"