class Solution:
    # dp[i] = (dp[i-1] + dp[i-2] + ... + dp[i-maxPts]) / maxPts
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        pre = 1.0   # 前缀和
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = pre / maxPts
            if i < k:
                pre += dp[i]
            else:
                res += dp[i]
            
            # 窗口优化
            if i >= maxPts:
                pre -= dp[i - maxPts]
        
        return res