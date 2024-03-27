N = int(input())
number = list(map(int, input().split()))
b = max(number)
count = 0
for i in range(N):
    a = number[i] / b *100
    count +=a
print(count/N)