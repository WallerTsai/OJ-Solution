class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [1,2]
        for _ in range(n-1):
            dp.append((dp[-1] + dp[-2]) % 1_000_000_007)
        
        # 根据乘法原理,两侧独立
        return dp[-1] ** 2 % 1_000_000_007