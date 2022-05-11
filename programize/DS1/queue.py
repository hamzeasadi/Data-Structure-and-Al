import sys, os, argparse


class Queue():

	def __init__(self):
		self.queue = []
		self.tail = -1
		self.head = 0

	def enqueue(self, item):
		self.queue.append(item)
		self.tail += 1

	def dequeue(self):

		if self.tail>=self.head:
			out = self.queue[self.head]
			self.head += 1
			return out

		else:
			return "queue is empty"

		

def main():
	queue = Queue()
	for i in range(2):
		queue.enqueue(i)

	for i in range(3):
		print(queue.dequeue())
	


if __name__=='__main__':
	main()


