init = list(map(int, input().split()))
n = init[0]
m = init[1]
bowl = [a for a in range(1, n + 1)]
for b in range (m):
    change = list(map(int, input().split()))
    i = change[0]
    j = change[1]
    if 1 <= i and i <= j and j <= n:
        bowl[i-1], bowl[j-1] = bowl[j-1], bowl[i-1]
print(" ".join(map(str, bowl)))