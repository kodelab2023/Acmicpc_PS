X = int(input())
N = int(input())
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    cnt += a*b
if X==cnt:
    print("Yes")
else:
    print("No")