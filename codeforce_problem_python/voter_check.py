import os
import sys
import random

try:
    a = int(input('Enter your age: '))

    age_limit = 70

    if a > 0:
        if a == 69:
            print('NOICE and Your eligible to get NID card.')

        elif a == 420:
            print('NOICE and Your definitly dead.')

        elif a >= 18 and a <= age_limit:
            print('You are eligible to get NID card.')

        elif a < 18 and a>0:
            print(f'You are {18-a} years away form getting a NID card.')

        elif a > age_limit and a < 100:
            print('You don\'t need a NID card. Your old.')

        else:
            print('You don\'t need a NID your dead or in bed.')
    else:
        print('Negative is not allowed')

except ValueError:
    print('\nEnter a number.')