from math import isqrt


class Solution:
    # 每次只喝 numExchange 瓶水
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            ans += 1
            numExchange += 1
            empty += 1

        return ans
    

class Solution:
    # 数学
    # https://leetcode.cn/problems/water-bottles-ii/solutions/2716773/an-ti-yi-mo-ni-jian-ji-xie-fa-pythonjava-n6g7/
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        b = e * 2 - 1
        k = (isqrt(b * b + (n - e) * 8) - b + 2) // 2
        return n + k