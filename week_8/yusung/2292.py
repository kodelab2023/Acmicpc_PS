N = int(input())
nums = 1
cnt =1
while N > nums:
    nums += 6 * cnt
    cnt += 1
print(cnt)