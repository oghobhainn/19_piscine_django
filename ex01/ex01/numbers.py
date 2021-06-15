#! /usr/bin/env python3

def numbers():
    f = open("numbers.txt", "r")
    arr = f.read().split(',')
    for i in arr:
        print(i)
    f.close()

if __name__ == '__main__':
    numbers()
