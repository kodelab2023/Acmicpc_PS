e, s, m = map(int, input().split())
a = 0
b = 0
c = 0
result = 0

if e == 1 and s == 1 and m == 1:
    result = 0
    
while True:
    result = result + 1
    a = a + 1
    b = b + 1
    c = c + 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
    if a == e and b == s and c == m:
        print(result)
        break      