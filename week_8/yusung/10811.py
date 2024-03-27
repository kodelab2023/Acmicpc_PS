N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(i+1)
    
for i in range(M):
    b, c = map(int, input().split())
    start_index = b-1
    end_index = c
    a[start_index:end_index] = a[start_index:end_index][::-1]

print(*a)