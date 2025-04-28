count = 0
n = int(input())
list = []

for i in range(n):
    s = input()
    list.append(s)

for i in range(n):
    if i < n - 1:
        if list[i] != list[i+1]:
            count += 1

#print(list)
print(count+1)