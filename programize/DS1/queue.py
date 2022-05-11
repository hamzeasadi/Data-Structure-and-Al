import sys, os, argparse


class Queue:
	def __init__(self):
		self.queue = []
		self.front = -1
		self.rear = -1

	def isEmpty(self):

		return self.rear == self.front-1

	def enqueue(self, item):
		if self.front < 0:
			self.front = 0

		self.rear += 1
		return self.queue.append(item)
	
	def dequeue(self):
		
		if self.isEmpty():
			
			return "queue is empty"

		else:
			out = self.queue[self.front]
			self.front += 1
			return out
		
		

def main():
	queue = Queue()
	for i in range(2):
		queue.enqueue(i)

	for i in range(3):
		print(queue.dequeue())
	


if __name__=='__main__':
	main()


