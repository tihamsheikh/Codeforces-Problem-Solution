import sys
import os
import random

def main():
    a = 'codeforces'
    b = len(a)
    try:
        n = int(input())

        if n > 0 and n <= 1000:

            for j in range(n):
                count = 0
                c = input().lower()

                if len(c) == 10:
                    for i in range(b):

                        if a[i] != c[i]:
                            count += 1

                print(count)
        else:
            pass
    except ValueError:
        pass

if __name__ == '__main__':
    main()