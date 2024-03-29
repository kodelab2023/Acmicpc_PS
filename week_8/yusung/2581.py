M = int(input())
N = int(input())
a = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(M, N+1):
    if is_prime(i):
        a.append(i)
        
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))