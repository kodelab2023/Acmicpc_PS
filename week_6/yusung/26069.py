N = int(input())
dance = {'ChongChong'}
for i in range(1, N+1):
    a, b  = input().split()
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)
    
print(len(dance))