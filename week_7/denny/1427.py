import sys
input = sys.stdin.readline

num = int(input().rstrip())
numlist = []
for i in str(num):
    numlist.append(int(i))
    
numlist.sort(reverse=True)

for i in numlist:
    print(i,end='')