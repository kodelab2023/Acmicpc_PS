a, b = map(int, input().split())
if a > b:
    c = a - b
elif b > a:
    c = b - a
print(c)