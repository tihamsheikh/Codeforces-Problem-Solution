count = 0
no = 0

poc = int(input())

for ex in range(poc):
    count = 0
    no = 0
    mid = 0

    s = input()
    s2 = s

    length = len(s)

    for i in range(length):
        j = length - i - 1
        dup = length - 1
        # print(f'i: {i} j: {j}')
        #print(f's[i]: {s[i]} s[j]: {s2[j]}')

        if s[i] == s[j]:
            count += 1

        if length%2 != 0:
            mid = int(length/2) + 1
        else:
            mid = length/2
        #print(mid)

        q = i + 1

        if q < length:
            if s[i] != s2[q]:
                #print(f'-----------{s[i]} {s2[q]}')
                no += 2
                q -= 1

    left = length - no

    #print(f'no: {no}')


    if length <= 3 or left > 0 or count != length:
        print(f'NO')
    elif count == length and left <= 0:
        print(f'YES')

    #print(count, no, left, length, mid)

    # print(s, s2)
