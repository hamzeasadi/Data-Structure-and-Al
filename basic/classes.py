class Range():
    def __init__(self, N):
        self.max = N
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<self.max:
            self.n+=1
            return self.n
        else:
            raise StopIteration

class PowTwo(object):
    def __init__(self, max):
        self.__max = max
        self.count = 0

    def __call__(self, new_max):
        self.__max = new_max

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.__max :
            self.count+=1
            return pow(self.count, 2)
        else:
            raise StopIteration


def all_even():
	n=0
	while True:
		n+=1
		yield 2*n



def main():
	x = all_even()
	for i in range(10):
		print(next(x))
if __name__ == '__main__':
    main()
