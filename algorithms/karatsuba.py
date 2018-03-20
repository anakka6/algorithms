#!usr/bin/python2.6

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

#x = 52345
#y = 81756

#x= 7
#y = 13
def num_digits(x):
	n=1
	while (x/(pow(10,n)) != 0):
		#print x/(pow(10,n))
		n = n+1

	return n

print "No.of digits : ",num_digits(x)

n = num_digits(x)

def product(x,y):
	n1 = num_digits(x)
	n2 = num_digits(y)
	n = min(n1,n2)
	#print "n = ",n
	if n==1:
		prod = x*y
	else:
		if n%2 !=0:
			n = n-1
		a = x/(pow(10,(n/2)))
		b = x%(pow(10,(n/2)))
		c = y/(pow(10,(n/2)))
		d = y%(pow(10,(n/2)))
		p = a+b
		q = c+d
		ac = product(a,c) #recursive
		bd = product(b,d)
		pq = product(p,q)

		adbc = pq-ac-bd
		prod = pow(10,n)*ac + pow(10,(n/2))*adbc + bd

	return prod

print "Product from karatsuba: \n ",product(x,y)
print "Product from 3rd grade: \n ",x*y
