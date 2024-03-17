import statistics as st
import sys

input = sys.stdin.readline
N = int(input().rstrip())
a = []
for i in range(N):
    x = int(input().rstrip())
    a.append(x)
    

avr = round(st.mean(a))
med = st.median(a)
modes = st.multimode(a)
modes_sorted = sorted(modes)
second_min_mode = modes_sorted[1] if len(modes_sorted) > 1 else modes_sorted[0]
min_value = min(a)
max_value = max(a)
range_val = max_value-min_value

print(avr)
print(med)
print(second_min_mode)
print(range_val)

    