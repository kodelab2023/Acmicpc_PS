A=[list(map(int, input().split())) for _ in range(9)]

max_value = A[0][0]
max_i = 0
max_j = 0

for i in range(9):
    for j in range(9):
        if max_value <= A[i][j]:
            max_value = A[i][j]
            max_i = i+1
            max_j = j+1

print(max_value)
print(max_i, max_j)