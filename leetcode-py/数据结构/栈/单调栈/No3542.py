from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        MIN = inf
        for num in nums:
            if num == 0:
                continue
            if num < MIN:
                MIN = num

        if MIN == inf:
            return 0
        
        pre = inf
        ans = 1
        for num in nums:
            if num > MIN and num != pre:
                ans += 1
            pre = num

        return ans  # 错误
    

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = [-1]
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if num >= st[-1]:
                st.append(num)
                continue
            while num < st[-1]:
                st.pop()
            ans += 1
        return ans + len(set(st)) - 1   # 错误


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = [-1]
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if num > st[-1]:    # 相等不用入栈
                st.append(num)
                continue
            while num < st[-1]:
                st.pop()
                ans += 1
        return ans + len(st) - 1    # 错误 # 中途来的0也要考虑
    

class Solution:
    # 灵神
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for x in nums:
            while st and x < st[-1]:
                st.pop()
                ans += 1
            # 如果 x 与栈顶相同，那么 x 与栈顶可以在同一次操作中都变成 0，x 无需入栈
            if not st or x != st[-1]:
                st.append(x)
        return ans + len(st) - (st[0] == 0)  # 0 不需要操作
    

class Solution:
    # leetcode 大佬
    # 以身为栈
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        top = -1  # 栈顶下标

        for x in nums:
            # 小于栈顶，说明需要增加一次操作
            while top >= 0 and x < nums[top]:
                top -= 1  # 出栈
                ans += 1
            # 栈空，说明这是一个新块的开始
            # 比栈顶大的新值，是 “上坡” 的新台阶，压入等待处理
            if top < 0 or x != nums[top]:
                top += 1
                nums[top] = x  # 入栈
        
        return ans + top + (nums[0] > 0)
    

class Solution:
    # leetcode 官方
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            # 碰到比栈顶小的，必出栈
            while s and s[-1] > a:
                s.pop()
            # 0 不用入栈， 入栈 ans 就 + 1 了
            if a == 0:
                continue
            # 入栈必消耗
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
