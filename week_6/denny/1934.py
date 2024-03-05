cnt = int(input())
for i in range(cnt):
    a, b = map(int, input().split())
    tmp = a * b
    while (b != 0):
        r = a % b
        a = b
        b = r
    print(int(tmp / a))