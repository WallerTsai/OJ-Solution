from itertools import count


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        m = k % 10
        if m not in (1, 3, 7, 9):
            return -1

        # 暴力
        ans = n = len(str(k))
        i = int("1" * n)
        while i % k:
            i = i * 10 + 1
            ans += 1
        return ans  # 1266ms
    
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        m = k % 10
        if m not in (1, 3, 7, 9):
            return -1

        ans = n = len(str(k))
        i = int("1" * n)
        while i % k:
            i = (i * 10 + 1) % k
            ans += 1
        return ans  # 4ms

class Solution:
    # 灵神
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        x = 1 % k
        for i in count(1):  # 一定有解
            if x == 0:
                return i
            x = (x * 10 + 1) % k

        






