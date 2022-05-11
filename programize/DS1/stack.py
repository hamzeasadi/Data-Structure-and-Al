import sys, os
import argparse
import random



class Stack():

	def __init__(self):
		self.stack = []
		self.top = -1
	
	def isEmpty(self):
		return self.top == -1;

	def push(self, item):
		self.stack.append(item)
		self.top += 1

	def pop(self):
		if not self.isEmpty():
			out = self.stack[self.top]
			del self.stack[self.top]
			self.top -= 1

			return out

		else:
			return f"stack is empty"

	def peek(self):
		if not self.isEmpty():
			return self.stack[self.top]


def main():
	mystack = Stack()
	for i in range(3):
		mystack.push(random.randint(1, 10))

	print(mystack.pop())

	
if __name__ == '__main__':
	main()
