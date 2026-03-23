from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        MX = -1
        li = []
        for i, x in enumerate(nums):
            MX = max(MX, x)
            a = gcd(MX, x)
            li.append(a)
        li.sort()
        n = len(li)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            ans += gcd(li[i], li[j])
            i += 1
            j -= 1
        return ans


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        MX = -1
        n = len(nums)
        li = [0] * n
        for i, x in enumerate(nums):
            MX = max(MX, x)
            li[i] = gcd(MX, x)
        li.sort()
        return sum(gcd(li[i], li[-1 - i]) for i in range(n // 2))
    

