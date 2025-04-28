count = 0

n = int(input())

s = str(n)

# print(s, n+1)

length = len(s)

for i in range(length):
    # print(f'i: {i}')
    if s[i] == '4' or s[i] == '7':
        count += 1
        # print(f'count: {count}')

if count == 4 or count == 7:
    print(f'YES')
else:
    print(f'NO')
