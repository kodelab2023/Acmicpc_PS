import sys
input = sys.stdin.readline
wlist = {}

n, m = map(int, input().rstrip().split())
for i in range(n):
    word = input().rstrip()
    if (len(word) < m):
        continue
    if word in wlist:
        wlist[word] += 1
    else:
        wlist[word] = 1

wlist = sorted(wlist.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in wlist:
    print(i[0])