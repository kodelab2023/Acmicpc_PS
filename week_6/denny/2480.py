from collections import Counter

a, b, c = map(int, input().split())
result = 0

if a == b and b == c and c == a:
    result = 10000 + a * 1000
elif a == b or b == c or c == a:
    arr = [a, b, c]
    tmp = Counter(arr)
    mitm = tmp.most_common(n=1)
    result = 1000 + mitm[0][0] * 100
else:
    result = max(a, b, c) * 100
print(result)    