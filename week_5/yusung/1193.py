X = int(input())
i = 1
while X >i:
    X -=i
    i +=1

if i%2 == 1:
    a = i - X +1
    b = X
elif i%2 == 0:
    a = X
    b = i - X +1
print(f'{a}/{b}')