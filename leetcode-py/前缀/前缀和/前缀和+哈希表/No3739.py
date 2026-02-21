from collections import defaultdict
from typing import List

# 灵神解法
# https://leetcode.cn/problems/count-subarrays-with-majority-element-ii/solutions/3826966/mei-ju-you-wei-hu-zuo-on-zuo-fa-pythonja-ojfh/
# 类似 No525 将target视为1其他为-1


# 计算有多少对 (i,j) 满足 0≤i<j≤n 且 s[j]−s[i]>0

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        sl = SortedList([0])  # 为什么加个 0？见 525 题我的题解
        ans = s = 0
        for x in nums:
            s += 1 if x == target else -1
            ans += sl.bisect_left(s)
            sl.add(s)
        return ans  # 678ms

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 为什么加个 0？见 525 题我的题解
        ans = s = f = 0
        for x in nums:
            if x == target:
                f += cnt[s]
                s += 1
            else:
                s -= 1
                f -= cnt[s]
            ans += f
            cnt[s] += 1
        return ans
    

# mipha大佬解法

# 前缀和 + 树状数组
# 映射： 前缀和 [-n,n] => [0,2n] => 树状数组 [1,2n+1] 
class NumArray:

    # 获取最低位 1 的位置
    @staticmethod
    def lowbit(x):
        return x & -x
    
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    # 添加值
    def add(self, index: int, value: int) -> None:
        index += 1
        while index <= self.n:
            self.tree[index] += value
            index += self.lowbit(index)

    # 求前缀和
    def query(self, index: int) -> int:
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 映射： 前缀和 [-n,n] => [0,2n] => 树状数组 [1,2n+1] 
        N = 2 * n + 1
        na = NumArray(N)

        pre = 0
        na.add(n, 1)

        ans = 0
        for num in nums:
            if num == target:
                pre += 1
            else:
                pre -= 1

            # [-n,pre-1] => [0,pre-1+n]
            temp = pre - 1 + n
            if temp >= 0:
                ans += na.sumRange(0, temp)

            na.add(pre + n, 1)

        return ans  # 1323ms



