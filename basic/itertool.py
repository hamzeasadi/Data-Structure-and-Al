import itertools
from itertools import count


def mycount(start, step):
	i=0
	while True:
		yield start + i*step	
		i+=1

def palindrome(n):
	out = ((10**n)//9)**2
	return out

def main():
	for i in mycount(1, 1):
		print(palindrome(i))
		if i>8:
			break	


if __name__ == '__main__':
	main()
