import os
import math


def wordCount(sentence):
    x = sentence.strip().count(' ') + 1
    print(x)

def coneVolume(r, h):
    volume = 3.14*r**2*(h/3)
    print(volume)

def spoky(s):
    word = 'sp' + 'o'*s + 'ky'    
    print(word)

def main():
    s = int(input().strip())
    spoky(s) 

if __name__ == '__main__':
    main()
