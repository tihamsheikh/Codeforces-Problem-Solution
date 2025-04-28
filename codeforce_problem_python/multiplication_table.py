import os
import sys
import random

# Multiplication Table

a = 1

try:
    b = int(input('Enter a to multiply: '))
    c = int(input('Enter the table length: '))
except ValueError:
    print('Enter a number.')

try:
    while( 0 <= a <= c):
        if a <= 9:
            print(f'{b} x 0{a} = {a*b}')
        else:
            print(f'{b} x {a} = {a * b}')
        a += 1
except NameError:
    pass