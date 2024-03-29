N, K = map(int, input().split())
Npq = []
for i in range(1, N+1):
    if N % i == 0:
        Npq.append(i)

if K > len(Npq):
    print(0)
else:
    print(Npq[K-1])