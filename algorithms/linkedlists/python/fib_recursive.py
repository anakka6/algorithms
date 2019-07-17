#/usr/bin/python3.6

def fib_recursive(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)


print(fib_recursive(8))