from functools import cache
from itertools import accumulate


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        @cache
        def dfs(i:int,numC:int):
            if numC == numCarpets or i >= n:
                return 0
            
            while i < n and floor[i] == '0':
                i += 1
            # 选
            count = 0
            for x in range(i,n):
                if floor[x] == "0" or count == carpetLen:
                    break
                count += 1

            return max(count+dfs(i+count,numC+1),dfs(i+1,numC)) 
        
        return int(floor,2).bit_count() - dfs(0,0)  # 简单示例通过

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        @cache
        def dfs(i:int,numC:int):
            if numC == numCarpets or i >= n:
                return 0
            
            while i < n and floor[i] == '0':
                i += 1
            # 选
            count = 0
            for x in range(i,min(i+carpetLen,n)):
                if floor[x] == '1':
                    count += 1

            return max(count+dfs(i+carpetLen,numC+1),dfs(i+1,numC)) 
        
        return int(floor,2).bit_count() - dfs(0,0) # 超时
    
# 以上思路都是从左到右然后计数1的个数

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        floor = list(map(int, floor))
        @cache
        def dfs(i:int,numC:int):
            # 不能不盖
            if n-i <= numC * carpetLen:
                return 0
            if numC == 0:
                return dfs(i+1,numC) + floor[i]
            return min(dfs(i+1,numC)+floor[i],dfs(i+carpetLen,numC-1))
        return dfs(0,numCarpets) # 1590ms
    # 递归过程中记录不选该位置的数

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        floor = list(map(int, floor))
        # dp[i][j] i:地毯数量,j:瓷砖数量
        dp = [[0] * n for _ in range(numCarpets+1)] # 第二维度大小尽量比第一维度大小大
        dp[0] = list(accumulate(floor)) # 0条地毯可以盖
        for i in range(1,numCarpets+1):
            for j in range(carpetLen*i,n):
                dp[i][j] = min(dp[i][j-1] + floor[j],dp[i-1][j-carpetLen])
        return dp[-1][-1] # 866ms
    
# 看状态方程就知道需要的空间大小
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        floor = list(map(int, floor))

        dp = list(accumulate(floor))
        for i in range(1,numCarpets+1):
            new_dp = [0] * n
            for j in range(carpetLen*i,n):
                new_dp[j] =  min(new_dp[j-1]+floor[j],dp[j-carpetLen])
            dp = new_dp
        return dp[-1] # 759ms