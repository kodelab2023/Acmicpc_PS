value = 'W'
board = [[value for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 'B'
countB = sum(row.count('B') for row in board)
print(countB)