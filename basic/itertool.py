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

	N = int(input("enter the lenght of the whole string: ")).strip()	
	x = input(f"enter the string with lenght {N}: ").strip().split()
	k = int(input("enter the subset lenght: ").strip())
	
	x.sort()
	ferq = lambda x: x[0]
	C = itertools.groupby(x, freq)
	for c in C:
		if key=='a':
			prob = 0.
			for i in range(1, k)
				math.comb(k, i)*(len(list(group))





if __name__ == '__main__':
	main()
