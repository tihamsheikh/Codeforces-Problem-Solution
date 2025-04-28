import sys
import os
import random

a = 0

try:
    a = int(input('Enter a number limit to find even and odd: '))

    if a > 0:
        print()
        print('The even numbers: ')
        for i in range(a):
            if not i%2 and i != 0:
                print(f'{i} ', end='')
        print(end='\n\n')

        print('The odd numbers: ')
        for i in range(a+1):
            if i%2:
                print(f'{i} ', end='')
        print(end='\n\n')
    elif a == 0:
        print('Zero doesn\'t have a even or odd.')
    else:
        print('The negative even: ')
        for i in range(-1, a, -1):
            if not i%2:
                print(f'{i} ', end='')
        print(end='\n\n')

        print('The negative odd: ')
        for i in range(-1, a-1, -1):
            if i%2:
                print(f'{i} ', end='')
        print(end='\n\n')

except ValueError or NameError:
    print('\nEnter a number. Like, 123 idiot.')
