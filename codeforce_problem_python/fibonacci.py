import sys
import os
import random

# this prints the sum of fibonacci series
a = int(input("Enter Searis Limit: "))

fsum = 0
s1 = 0
s2 = 1

print(f'{s1}\n{s2}')

for i in range(2, a):

    s3 = s1 + s2
    fsum += s3

    print(s3)

    s1 = s2
    s2 = s3
print(f'Sum of Fibonacci Series is {fsum+1}')

# another version of fibonacci series
n = int(input('Enter series range: '))

def fibo(n):

    n1 = 0
    n2 = 1

    print(f'{n1}\n{n2}')

    for i in range(2, n):
        n3 = n1 + n2
        print(n3)

        n1 = n2
        n2 = n3

fibo(n)


