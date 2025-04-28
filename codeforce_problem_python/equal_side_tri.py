import os
import sys
import random

try:
    n = int(input('Enter a height: '))

    for i in range(n):

        for j in range(1, (n-i+1)):           # 1 2 3
            print(f'{j} ', end='')            # 1 2
                                              # 1
        print()

    for i in range(n):
        k = (n - i)

        for j in range(k, 0, -1):             # 3 3 3
                                              # 2 2
                                              # 1
            print(f'{k} ', end='')

        print()

    for i in range(n):
        k = n - i

        for j in range(k, 0, -1):             #3 2 1
            print(f'{j} ', end='')            #2 1
                                              #1
        print()

except ValueError:
    print('Enter a number!!')