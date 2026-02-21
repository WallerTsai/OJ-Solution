PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(i.bit_count() in PRIMES for i in range(left, right + 1))




MX = 100_001
is_p = [True] * MX
is_p[0] = is_p[1] = False
prime_numbers = []
for i in range(2, MX):
    if is_p[i]:
        prime_numbers.append(i)
        for j in range(i * i, MX, i):
            is_p[j] = False
prime_numbers_set = set(prime_numbers)
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(i.bit_count() in prime_numbers_set for i in range(left, right + 1))