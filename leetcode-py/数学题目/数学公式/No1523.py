class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return sum( x % 2 == 1 for x in range(low, high + 1))   # 超时
    
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + (low % 2 == high % 2 == 1)
    
class Solution:
    # 数学公式
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2