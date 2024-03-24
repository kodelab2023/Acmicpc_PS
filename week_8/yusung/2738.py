N, M = map(int, input().split())

A = []
B = []
for i in range(N):
    num = list(map(int, input().split()))
    A.append(num)

for i in range(N):
    num = list(map(int, input().split()))
    B.append(num)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
