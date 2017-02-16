#!/usr/bin/python
import datetime
class MyNum(object):
	
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		
	def addMethod (self):
		return self.a + self.b + self.c
		
	def multiply(self):
		return self.a*self.b*self.c
	
	def middle(self):
		if self.a == self.b or self.b == self.c or self.a == self.c:
			return False
		elif self.a <= self.b <= self.c or self.c <= self.b <= self.a:
			return self.b
		elif self.b <= self.a <= self.c or self.c <= self.a <= self.b:
			return self.a
		else:
			return self.c
	
	def largest (self):
		return max(self.a, self.b, self.c)
	
	def smallest(self):
		return min(self.a, self.b, self.c)
	
	def average(self):
		return ((self.a + self.b + self.c)/3)
		
	def triangle(self):
		if self.a == self.b == self.c:
			return ("Equilateral triangle")
		elif self.a != self.b and self.b != self.c and self.a != self.c:
			return ("Scalene triangle")
		else:
			return ("isosceles triangle") 
		
	def __add__(self, other):
		myList = [self.a + other.a, self.b + other.b,self.c + other.c ]
		return myList
	
	def __sub__(self, other):
		myList = [self.a - other.a, self.b - other.b,self.c - other.c ]
		return myList
		
	def ourTime(self):
		now = datetime.datetime.now()
		if now.minute == self.a or now.minute == self.b or now.minute == self.c:
			return True
		else:
			return False
		
	def vertex(self):
		h = float(-self.b/2*self.a)
		
		k = float((self.a*h)**2 + self.b*h + self.c)
		
		return "(%s, %s)" % (h,k)


num1 = MyNum(3, 1, -2)
num2 = MyNum(3,4,5)	
print num1.addMethod()
print num1.multiply()
print num1.middle()
print num1.largest()
print num1.smallest()
print num1.average()
print num1.triangle()
print num1 + num2
print num1 - num2
print num1.ourTime()
print num1.vertex()


	