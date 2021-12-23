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




def main():
    for i in PowTwo(10):
        print(i)

if __name__ == '__main__':
    main()
