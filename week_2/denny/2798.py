from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
a = 0

for i in combinations(card, 3):
    if a < sum(i) and sum(i) <= m:
        a = sum(i)
print(a)       
