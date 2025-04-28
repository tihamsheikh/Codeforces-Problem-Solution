# out = 92%

# while True:
#     e = int(input('Exit- 0 : '))
#     if e != 1:
#         if e == 0:
#             break
for i in range(1, 301):

    p = 0.9
    # a = float(input('--cash: '))

    out = i * p + i



    print(f'{i} - %.2f' %out)
