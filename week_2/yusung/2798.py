from itertools import combinations

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = 0
for i in combinations(a, 3):
    if b < sum(i) and sum(i) <= M:
        b = sum(i)         
                
print(b)