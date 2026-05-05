
# cache
from functools import cache


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False
        
        @cache
        def dfs(i: int):
            if i == n - 1:
                return True
            
            for j in range(i + minJump, min(i + maxJump, n- 1) + 1):
                if s[j] == '0' and dfs(j):
                    return True
                
            return False
        
        ans = dfs(0)
        dfs.cache_clear()
        return ans  # 超时
    
# 我们定义 dp[i] 表示是否能跳到索引 i（1 表示能，0 表示不能）。
# 要想跳到 i，必须满足两个条件：

# s[i] 必须是 '0'。
# 在可以跳到 i 的有效区间 [i - maxJump, i - minJump] 内，至少存在一个点 j，满足 dp[j] == 1。
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False
        
        dp = [0] * n
        dp[0] = 1

        pre = [0] * (n + 1)
        pre[1] = 1

        for i in range(1, n):
            if s[i] == "0":
                left = max(0, i - maxJump)
                right = i - minJump
                if right >= 0:
                    total = pre[right + 1] - (pre[left] if left > 0 else 0)
                    if total > 0:
                        dp[i] = 1
            pre[i + 1] = pre[i] + dp[i]

        return bool(dp[-1])


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        
        n = len(s)
        dp = [False] * n
        dp[0] = True

        active = 0
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                active += 1
            
            if i > maxJump and dp[i - maxJump - 1]:
                active -= 1

            if s[i] == '0' and active > 0:
                dp[i] = True

        return dp[-1]