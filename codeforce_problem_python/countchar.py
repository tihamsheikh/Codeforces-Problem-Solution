import os
import random
import sys

a = input('Enter a sentence: ')
count = 0
vowel = 0
consonant = 0
digits = 0
words = 1
other = 0

for i in a:

    if i.lower() in 'aeiou':
        vowel += 1
    else:
        if i.lower() not in 'aeiou' and 'A' <= i <= 'z':
            consonant += 1
        else:
            if i >= '0' and i <= '9':
                digits += 1
            else:
                if i.lower() == ' ':
                    words += 1

                else:
                    other += 1

print(f'There is {vowel} vowel\'s in the sentence')
print(f'There is {consonant} consonant\'s in the sentence')
print(f'There is {digits} digits in the sentence')
print(f'There is {words} words in the sentence')
print(f'There is {other} other charecter\'s in the sentence')