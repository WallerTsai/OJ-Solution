MX = 100_001

isprime = [True] * (MX + 1)
primes = list()
# 埃拉托斯特尼筛法
for i in range(2, MX + 1):
    if isprime[i]:
        primes.append(i)
    for j in range(i + i, MX + 1, i):
        isprime[j] = False