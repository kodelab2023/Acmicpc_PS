init = list(map(int, input().split()))
n = init[0]
m = init[1]
bowl = [0 for b in range(n)]
for a in range (m):
    ball = list(map(int, input().split()))
    i = ball[0]
    j = ball[1]
    k = ball[2]
    if 1 <= i and i <= j and j <= n and 1 <= k and k <= n:
        bowl[i-1:j] = [k] * (j - i + 1)
print(" ".join(map(str, bowl)))