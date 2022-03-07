import os

def wordCount(sentence):
    x = sentence.strip().count(' ') + 1
    print(x)


def main():
    wordCount(input("enter your sentence: "))

if __name__ == '__main__':
    main()
