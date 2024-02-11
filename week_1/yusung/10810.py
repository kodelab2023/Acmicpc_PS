import sys

N, M = map(int, input().split())
a = [0 for _ in range(N)]


for m in range(M):
    I, J, K = int(input().split())
    if I>N:
        sys.exit("I value must be less than N value")
    elif J>N:
        sys.exit("J value must be less than N value")
    elif K>N:
        sys.exit("K value must be less than N value")
    elif I>J:
        sys.exit("I value must be less than J value")
    else:
        for h in range(I, J+1):
            a[h-1] = K

print(*a)
        