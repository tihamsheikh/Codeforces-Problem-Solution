import os
import sys
import random

a = int(input('Enter the exam paper score: '))

if 0 <= a <= 100:
    if 90 <= a <= 100:
        print('You got a \'A++\'')
    elif 80 <= a < 90:
        print('You got a \'A+\'')
    elif 70 <= a < 80:
        print('You got a \'A\'')
    elif 60 <= a < 70:
        print('You got a \'A-\'')
    elif 50 <= a < 60:
        print('You got a \'B\'')
    elif 40 <= a < 50:
        print('You got a \'C\'')
    else:
        print('You Failed the exam.')
        print('You are qualified to stat working.')
else:
    print('The Score is between 0 to 100.')