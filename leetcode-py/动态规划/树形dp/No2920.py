from functools import cache
from typing import List


class Solution:
    # 灵神解法感悟
    # 递归
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        # 以邻接表的方式建图
        group = [[] for _ in coins]
        for x,y in edges:
            group[x].append(y)
            group[y].append(x)  # 无向

        @cache
        def dfs(i:int,count:int,father:int) -> int:
            res1 = (coins[i] >> count) - k  # 第一种方式
            res2 = coins[i] >> (count+1)  # 第二种方式
            # 扫描子树
            for child in group[i]:
                if child != father:
                    res1 += dfs(child,count,i)  # 第一种方式
                    if count < 13:
                        res2 += dfs(child,count+1,i)  # 第二种方式
            return max(res1,res2)
        
        return dfs(0,0,-1)  # 2483ms
    
class Solution:
    # 递归
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        # 以邻接表的方式建图
        group = [[] for _ in coins]
        for x,y in edges:
            group[x].append(y)
            group[y].append(x)  # 无向

        @cache
        def dfs(i:int,count:int,father:int) -> int:
            res1 = (coins[i] >> count) - k  # 第一种方式
            res2 = coins[i] >> (count+1)  # 第二种方式
            # 扫描子树
            for child in group[i]:
                if child != father:
                    res1 += dfs(child,count,i)  # 第一种方式
                    if count < 13:
                        res2 += dfs(child,count+1,i)  # 第二种方式
            return max(res1,res2)
        dfs.cache_clear()   # 羊神说这样可以使python跑快一点
        return dfs(0,0,-1)
    
# 结合leetcode最快
class Solution:
    # 回溯
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        MAX_DIV = 14    # 14次必为0

        # 以邻接表的方式建图
        group = [[] for _ in coins]
        for x,y in edges:
            group[x].append(y)
            group[y].append(x)  # 无向

        def dfs(index:int,depth:int,father:int) -> list:
            depth = min(depth,MAX_DIV-1)
            child_value = [0] * (depth+1)
            for child in group[index]:
                if child != father:
                    # 递归
                    grandchild_value = dfs(child,depth+1,index)
                    # 回溯
                    for i in range(len(grandchild_value)):
                        child_value[i] += grandchild_value[i]
            # 选择方式
            for i in range(depth):
                child_value[i] = max(child_value[i] + (coins[index]>>i) - k , child_value[i+1] + (coins[index]>>(i+1)))
            child_value.pop()
            
            return child_value
        
        return dfs(0,1,-1)[0]

fun = Solution()
out = fun.maximumPoints([[0,1],[1,2],[2,3]],[10,10,3,3],5)