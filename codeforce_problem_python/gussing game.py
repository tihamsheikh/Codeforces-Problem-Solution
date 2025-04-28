a = ''
f = 'fuka'
count = 0

while a.lower() != f and count < 4:
    a = input('Enter a word: ')
    count += 1

if count == 4 and a != f:
    print('You failed to guess in time!')
else:
    print('Well, done!!')