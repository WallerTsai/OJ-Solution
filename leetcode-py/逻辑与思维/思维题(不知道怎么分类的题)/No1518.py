class Solution:
    # 每次都喝完每瓶水
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = 0
        while numBottles:
            ans += numBottles
            a, b = divmod(numBottles + empty, numExchange)
            empty = b
            numBottles = a
        return ans
    
class Solution:
    # 每次只喝 numExchange 瓶水
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            ans += 1
            empty += 1

        return ans
    
class Solution:
    # 数学
    # https://leetcode.cn/problems/water-bottles/solutions/339339/huan-jiu-wen-ti-by-leetcode-solution/
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return (numBottles - numExchange) // (numExchange - 1) + 1 + numBottles if numBottles >= numExchange else numBottles
    


class Solution:
    # 灵神
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
        



