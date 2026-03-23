from functools import cache


class Solution:
    # 真分治
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        li = list(s)
        pre_sum = [0]
        for x in s:
            if x == '1':
                pre_sum.append(pre_sum[-1] + 1)
            else:
                pre_sum.append(pre_sum[-1])

        def dfs(left, right):
            if left == right:
                return encCost if li[left] == '1' else flatCost
            
            res = flatCost
            if pre_sum[right + 1] - pre_sum[left] > 0:
                res = (right - left + 1) * (pre_sum[right + 1] - pre_sum[left]) * encCost

            if (right - left + 1) % 2 == 0:
                mid = (right + left) // 2
                res = min(res, dfs(left, mid) + dfs(mid + 1, right))

            return res
        
        ans = dfs(0, n - 1)
        return ans



class Solution:
    # 记忆化递归
    # cache命中严重影响过题时间
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        
        @cache
        def dfs(s: str) -> int:
            length = len(s)
            X = s.count('1')
            
            res = flatCost if X == 0 else length * X * encCost
            
            if length % 2 == 0:
                mid = length // 2
                res = min(res, dfs(s[:mid]) + dfs(s[mid:]))
                
            return res
        
        ans = dfs(s)
        dfs.cache_clear()
        return ans