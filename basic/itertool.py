import itertools
import random

from itertools import count


def mycount(start, step):
	i=0
	while True:
		yield start + i*step	
		i+=1

def palindrome(n):
	out = ((10**n)//9)**2
	return out

def mysub(a, b):
	return b-a

def orderper(s, k):
	x = list(s)
	x.sort()
	out = itertools.combinations(x, k)
	return out
		

def main():

	x = list(input().strip())
	print(x)
	x.sort()
	print(x)



if __name__ == '__main__':
	main()
