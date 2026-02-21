from itertools import count
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for num in nums:
            cnt[num % value] += 1
        for i in count(0):
            if not cnt[i % value]:
                return i
            cnt[i % value] -= 1


class Solution:
    def findSmallestInteger(self, nums: List[int], m: int) -> int:
        cnt = [0] * m
        for x in nums:
            cnt[x % m] += 1

        i = cnt.index(min(cnt))
        return m * cnt[i] + i

fun = Solution()
fun.findSmallestInteger([3,0,3,2,4,2,1,1,0,4], 5)
