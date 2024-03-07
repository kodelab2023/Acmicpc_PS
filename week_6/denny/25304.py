total = int(input())
total_tmp = 0
a = int(input())
for i in range(a):
    price, num = map(int, input().split())
    total_tmp += price*num
if total == total_tmp:
    print("Yes")
else:
    print("No")        