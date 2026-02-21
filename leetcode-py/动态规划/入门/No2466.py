from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(length:int):
            if length > high:
                return 0
            temp = 0
            if low <= length <= high:
                temp = 1
            
            return temp + dfs(length + zero) + dfs(length + one)
        
        return dfs(0) % 1_000_000_007 # 内存爆了
    
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(length:int):
            if length > high:
                return 0
            temp = 0
            if low <= length <= high:
                temp = 1
            
            return (temp + dfs(length + zero) + dfs(length + one))% 1_000_000_007
        
        return dfs(0) # 215ms

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(length:int):
            if length < 0:
                return 0
            if length == 0:
                return 1
            
            return (dfs(length - zero) + dfs(length - one)) % 1_000_000_007
        
        return sum(dfs(i) for i in range(low,high + 1)) % 1_000_000_007 # 215 内存好很多
    
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        for i in range(1,high+1):
            if i >= zero:
                dp[i] = dp[i - zero]
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % 1_000_000_007
        return sum(dp[low:]) % 1_000_000_007 # 67ms
    
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        dp = [0] * (high + 1)
        dp[0] = 1  # 空字符串也算一种情况
        
        for length in range(high + 1):
            if dp[length] == 0:
                continue  # 如果当前长度不可达，跳过
            if length + zero <= high:
                dp[length + zero] = (dp[length + zero] + dp[length]) % MOD
            if length + one <= high:
                dp[length + one] = (dp[length + one] + dp[length]) % MOD
        
        result = 0
        for length in range(low, high + 1):
            result = (result + dp[length]) % MOD
        
        return result # 95ms 



