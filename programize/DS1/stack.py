import sys,os


class Stack():
	def __init__(self, **kwargs):
		self.size=kwargs['size']
		self.top = -1
		self.stack = []

	def isEmpty(self):
		return self.top < 0;

	def isFull(self):
		return self.top>=self.size

	def pop(self):
		if not self.isEmpty():
			element = self.stack[self.top]
			self.top -= 1
			return element
		else:
			print("stack is empty!!!")
			return None


	def push(self, x):
		if self.isFull():
			print("Stack is full!!!")
		else:
			self.top += 1
			self.stack.append(x)

	def peek(self):
		if not self.isEmpty():
			return self.stack[self.top]

def main():
	stack = Stack(size=10)
	for i in range(1,10):
		print(i)
		stack.push(i)
	
	for i in range(10):
		print(stack.pop())
	


if __name__ == '__main__':
	main()
