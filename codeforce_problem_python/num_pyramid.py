import os
import sys
import random

n = 0
try:
    n = int(input('Enter the pyramid height: '))
    n += 2
except ValueError:
    print('Enter a valid number!!!')

if n > -1:
    for p in range(1, n-1):

        for q in range(1, n-p):
            print(' ', end='')
        for w in range(1, n-q):
            print(f' {w}', end='')
            
        print()
else:
    print('Enter a valid number!!!')
