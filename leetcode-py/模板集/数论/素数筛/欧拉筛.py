MX = 100_001
isprime = [True] * (MX + 1)
primes = list()
for i in range(2, MX + 1):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if i * prime > MX:
                    break
                isprime[i * prime] = False
                if i % prime == 0:
                    break


