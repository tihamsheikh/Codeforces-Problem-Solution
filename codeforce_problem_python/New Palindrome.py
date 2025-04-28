def strCheck(s):
    count = 0
    fcount = 0
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
            #print(freq)
        else:
            freq[char] = 1
            #print(freq)

    for key in freq:
        if freq[key] > 1:
            count += 1

    if count >= 2:
        fcount += 1
    return fcount

n = int(input())

for i in range(n):
    s = input()
    yn = strCheck(s)

    if yn > 0:
        print("YES")
    else:
        print("NO")

