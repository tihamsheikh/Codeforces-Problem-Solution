import os
import sys
import random

file = open('names.txt', 'w')

print(file.mode)
print(file.name)

file.write('file is writen with bytes() fuc or method\n')
file.write('Here is another string in file. So, it is another text and more on that later. And it is a thing in python and\n'
           'other programming language and it is useful in various ways\n')

file.close()

file = open('names.txt', 'r+')

file_txt = file.read()

print(file_txt)

file.close()

os.remove('names.txt')