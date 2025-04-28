import os
import sys
import random

a = int(input())
count = 0

for i in range(a):
    b = input()

    # for j in b:
    #     print(j)
    if b == '++X' or b == 'X++':
        count += 1

    if b == '--X' or b == 'X--':
        count -= 1

print(count)
