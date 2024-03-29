def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

N = int(input())

f = prime_factors(N)
for i in range(len(f)):
    print(f[i])