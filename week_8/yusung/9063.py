n = int(input())
xnum = []
ynum = []

for i in range(n):
    a, b = map(int, input().split())
    xnum.append(a)
    ynum.append(b)

if n == 1:
    print(0)
else:
    x = max(xnum) - min(xnum)
    y = max(ynum) - min(ynum)
    print(x*y)