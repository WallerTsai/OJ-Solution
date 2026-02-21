from functools import cache
from itertools import pairwise
from math import inf
from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        pre_num = [0] + [i-j for j,i in pairwise(original)]
        res = 0
        n = len(original)
        def dfs(i,pre):
            if i == n:
                nonlocal res
                res += 1
                return
            a,b = bounds[i]
            next_num = pre + pre_num[i]
            if a <= next_num <= b:
                dfs(i+1,next_num)
            else:
                return
        for x in range(bounds[1][0],bounds[1][1] + 1):
            dfs(1,x)
        return res

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        pre_num = [0] + [i-j for j,i in pairwise(original)]
        res = 0
        n = len(original)
        @cache
        def dfs(i,pre):
            if i == n:
                nonlocal res
                res += 1
                return
            a,b = bounds[i]
            next_num = pre + pre_num[i]
            if a <= next_num <= b:
                dfs(i+1,next_num)
            else:
                return
        for x in range(bounds[0][0],bounds[0][1] + 1):
            dfs(1,x)
        return res
    
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        pre_num = [0] + [i-j for j,i in pairwise(original)]
        res = 0
        m = len(original)
        
        @cache
        def check(x:int):
            for i in range(1,m):
                next_x = x + pre_num[i]
                if next_x < bounds[i][0] or next_x > bounds[i][1]:
                    return False
                x = next_x
            return True

        for n in range(bounds[0][0],bounds[0][1] + 1):
            if check(n):
                res += 1
        return res
    
# 以上都是超时的
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        mn, mx = -inf, inf
        for x, (u, v) in zip(original, bounds):
            mn = max(mn, u - x)  
            mx = min(mx, v - x)
        return max(mx - mn + 1, 0)  
# https://leetcode.cn/problems/find-the-number-of-copy-arrays/solutions/3591446/

fun = Solution()
fun.countArrays([1,2,1,2],[[1,1],[2,3],[3,3],[2,3]])