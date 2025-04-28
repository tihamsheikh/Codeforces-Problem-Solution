import os
import sys
import random

# Word Finder
a = ''
score = 0
limit = 0
cap = 5  # change the maximum tries
ans = 'monalisa'  # change the answer here. Only strings are valid.
ans = ans.strip()

print('\nThe name of the famous painting by Leo Nardo the Vinci.\n')  # change the question here

while (a != ans and limit < cap):
    a = input('Enter answer: ')
    a = a.lower().strip()
    limit += 1

    if a == ans:
        break
    if limit == cap - 1:
        print('This is your last chance.\n')

if limit == cap and a.lower().strip() != ans:
    print('\n-- You ran out of Tries!! --')
    print(f'    -- Your score: {score} --')
else:
    if limit == 1:
        print(f'\n--- You won the game. It took you {limit} try. ---')
    else:
        print(f'\n--- You won the game. It took you {limit} tries. ---')
    if a == ans:
        score += 1
    print(f'         --- Your score: {score} ---')

