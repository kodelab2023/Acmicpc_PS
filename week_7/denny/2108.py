import sys
import statistics as st

input = sys.stdin.readline
a = int(input().rstrip())
list = []

for i in range(a):
    res = int(input().rstrip())
    list.append(res)

print(round(st.mean(list)))
print(st.median(list))

md = st.multimode(list)
if len(md) > 1:
    md.sort()
    print(md[1])
else:
    print(md[0])

print(max(list)-min(list))