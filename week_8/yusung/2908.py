A, B = list(map(int, input().split()))

A = list(reversed(str(A)))
B = list(reversed(str(B)))
if A > B :
    print("".join(A))
elif A < B :
    print("".join(B))
