import os
import sys
import random

m, n = map(int, input().split()) # n > m

if 0 <= m <= n <= 16:
    cal = n * m / 2
    i_cal = int(cal)
    print(f'{i_cal:.0f}')

