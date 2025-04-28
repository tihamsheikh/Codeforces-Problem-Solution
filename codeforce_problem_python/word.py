import os
import sys
import random

upper, lower = 0, 0

s = input()

for i in s:
    #print(i)
    if i >= 'A' and i  <= 'Z':
        upper += 1
    if i >= 'a' and i <= 'z':
        lower += 1
#print(upper, lower)

if upper > lower:
    ss = s.upper()
    print(ss)
elif lower > upper:
    ss = s.lower()
    print(ss)
elif lower == upper:
    ss = s.lower()
    print(ss)
