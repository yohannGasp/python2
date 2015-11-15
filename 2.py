#!/usr/bin/python3

class app:
	attr = 123
	def __init__(self, arg):
		self.arg = arg
	def m(self, x):
		print(self.attr * self.arg * x)

a = app(3)
a.attr = 2
a.m(2)




