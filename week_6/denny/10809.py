word = input()
check = 'abcdefghijklmnopqrstuvwxyz'

for i in check:
    if i in word:
        print(word.index(i), end = ' ')
    else:
        print(-1, end = ' ')        