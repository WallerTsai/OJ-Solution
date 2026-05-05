class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1000000007
        
        # dp[i] 表示第 i 天新增的知道秘密的人数
        dp = [0] * (n + 1)
        # pre[i] 表示前 i 天新增人数的总和（即 dp 数组的前缀和）
        pre = [0] * (n + 1)
        
        # 第一天只有 1 个人知道秘密
        dp[1] = 1
        pre[1] = 1
        
        for i in range(2, n + 1):
            # 计算今天能够分享秘密的人，他们最初发现秘密的时间区间 [left, right]
            
            # left：最早能分享的人，是今天刚好还没忘记的人
            left = max(1, i - forget + 1)
            
            # right：最晚能分享的人，是刚好度过 delay 冷却期的人
            right = i - delay
            
            # 如果存在合法的分享者，计算这批人的总数
            if right >= left:
                # 利用前缀和直接相减，代替 for 循环累加
                dp[i] = (pre[right] - pre[left - 1]) % MOD
            
            # 无论今天有没有新增，都要更新前缀和数组
            pre[i] = (pre[i - 1] + dp[i]) % MOD
            
        # 题目问的是第 n 天依然知道秘密的总人数
        # 也就是最后 forget 天内新增的人数总和（在第 n - forget + 1 天到第 n 天发现的）
        ans_left = max(1, n - forget + 1)
        
        # 再次利用前缀和求最后一段区间的总和
        ans = (pre[n] - pre[ans_left - 1]) % MOD
        
        # Python 中取模相减可能会产生负数，加上 MOD 再取模可以保证结果正确
        return (ans + MOD) % MOD