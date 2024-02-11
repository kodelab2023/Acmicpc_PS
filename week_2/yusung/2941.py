A = input()
Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in Croatia:
    A = A.replace(a, '0')
print(len(A))