list = {"ChongChong"}
num = int(input())
for i in range(num):
    A, B = input().split()
    if A in list:
        list.add(B)
    if B in list:
        list.add(A)
print(len(list))            