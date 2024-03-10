a = list(map(int, input().split()))
b = list(map(int, input().split()))
at, bt, cnt = 0, 0, 0
for i in range(9):
    at += a[i]
    if at > bt:
        cnt +=1
    bt += b[i]

if cnt>0:
    print("Yes")
else:
    print("No")