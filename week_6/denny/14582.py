j = list(map(int, input().split()))
g = list(map(int, input().split()))
j_total , g_total = 0, 0
iswin = False

for i in range(9):
    j_total += j[i]
    if j_total > g_total:
        iswin = True
    g_total += g[i]
if g_total > j_total and iswin == True:
    print('Yes')
else:
    print('No')