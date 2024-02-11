import sys

N, M = map(int, input().split())
a = [i for i in range(1, N+1)]

for m in range(M):
    I, J = map(int, input().split())
    if 1<=I and I<=J and J<=N:
        a[I-1], a[J-1] = a[J-1],a[I-1]
    else:
        sys.exit()
print(*a)