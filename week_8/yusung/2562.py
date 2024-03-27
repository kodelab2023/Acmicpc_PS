a = []
for i in range(9):
    A = int(input())
    a.append(A)
    
b = max(a)
c = a.index(b)
print(b)
print(c+1)