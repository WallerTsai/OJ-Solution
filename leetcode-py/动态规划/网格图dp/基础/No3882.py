from math import inf


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = inf
        visited = set()
        def dfs(i, j, xor):
            nonlocal ans
            # 剪枝
            if ans == 0:
                return
            if (i, j, xor) in visited:
                return
            if i < 0 or j < 0:
                return 
            
            visited.add((i, j, xor))
            xor ^= grid[i][j]
            if i == 0 and j == 0:
                ans = min(ans, xor)
                return
            dfs(i - 1, j, xor)
            dfs(i, j - 1, xor)
        dfs(m - 1, n - 1, 0)
        return ans  # 203ms
    

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        for i in range(m):
            for j in range(n):
                for s in dp[i][j]:
                    if i + 1 < m:
                        dp[i + 1][j].add(s ^ grid[i + 1][j])
                    if j + 1 < n:
                        dp[i][j + 1].add(s ^ grid[i][j + 1])
        return min(dp[-1][-1])  # 2430ms
    

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        
        for j in range(1, n):
            for val in dp[0][j-1]:
                dp[0][j].add(val ^ grid[0][j])
                
        for i in range(1, m):
            for val in dp[i-1][0]:
                dp[i][0].add(val ^ grid[i][0])
                
        for i in range(1, m):
            for j in range(1, n):
                for val in dp[i-1][j]:
                    dp[i][j].add(val ^ grid[i][j])
                
                for val in dp[i][j-1]:
                    dp[i][j].add(val ^ grid[i][j])
                    
        return min(dp[m-1][n-1])    # 1639ms
    

# 以上两种不同的dp写法Gemini总结：
# 第一种写法：刷表法(我要到哪里去？) 利用 dp[i][j] 里的每一个状态 s，去主动更新 dp[i+1][j] 和 dp[i][j+1]
# 第二种写法：填表法(我从哪里来？) dp[i][j] = dp[i-1][j] + dp[i][j-1]
