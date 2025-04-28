import os
import sys
import random

def main():

    n = int(input())

    if 0 < n <= 100:

        for i in range(n):
            a = input()
            a.strip()

            lwn = len(a)

            if 0 < lwn <= 10:
                print(a)
            elif 10 < lwn < 101:
                word(a)

def word(a):
    length = len(a)
    count = 0
    for i in range(length):
        count += 1

    print(f'{a[0]}{count-2}{a[length-1]}')

if __name__ == '__main__':
    main()