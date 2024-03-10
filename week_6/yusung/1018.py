N, M = map(int, input().split())

chessboard = []
changecount = []

for i in range(N):
    chessboard.append(input())
        
for i in range(N-7):
    for j in range(M-7):
        Wdraw = 0
        Bdraw = 0
        result = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) %2 ==0:
                    if chessboard[a][b] != 'W':
                        Wdraw +=1
                    if chessboard[a][b] != 'B':
                        Bdraw +=1
                else:
                    if chessboard[a][b] != 'B':
                        Wdraw +=1
                    if chessboard[a][b] != 'W':
                        Bdraw +=1       
        result = min(Wdraw, Bdraw)
        changecount.append(result)

print(min(changecount))