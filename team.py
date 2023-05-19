import os
import sys
import random

a = int(input())
count = 0
fin = 0

for i in range(a):

    count = 0
    for j in range(3):
        b = int(input())
        if b == 0 or b == 1:
            if b == 1:
                count += 1
        else:
            continue

    if count >= 2:
        fin += 1

print(fin)