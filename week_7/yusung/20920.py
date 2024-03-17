from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
a = []
for i in range(N):
    a.append(input().rstrip())

filtered_a = [item for item in a if len(item) >= M]

counts = Counter(filtered_a)

sorted_a = sorted(counts.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
unique_sorted_filtered_a = [item for item, _ in sorted_a]
for item in unique_sorted_filtered_a:
    print(item)