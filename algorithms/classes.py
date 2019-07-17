#!/usr/local/bin/python3

class Employee:

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)



emp1 = Employee('Abhinaya','Nakka',4000)

# print(emp1.email)
# print(emp1.fullname())

# print(Employee.fullname(emp1))

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

print(emp1.__dict__)