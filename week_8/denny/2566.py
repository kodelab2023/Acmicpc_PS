a = []

for ls in range(9):
    ls = list(map(int, input().split()))
    a.append(ls)

maxval = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if a[i][j] >= maxval:
            maxval = a[i][j]
            row = i + 1
            col = j + 1

print(maxval)
print(row, col)            