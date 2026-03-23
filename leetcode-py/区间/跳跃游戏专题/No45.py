from math import inf
from typing import List
# class Solution:
#     ## 错误
#     def jump(self, nums: List[int]) -> int:
#         res = 0
#         cur_node = 0
#         step = 0
#         while cur_node < len(nums)-1:
#             max_num = max(nums[cur_node:cur_node+nums[cur_node]+1])
#             step = max(max_num,nums[cur_node])
#             cur_node += step
#             res += 1

#         return res

# class Solution:
#     # 动态规划
#     # 太慢了
#     def jump(self, nums: List[int]) -> int:
#         length = len(nums)
#         # dp[i] 表示到小标i的点的最小步数
#         dp = [inf for _ in range(length)]
#         dp[0] = 0

#         for i in range(1,length):
#             for j in range(i):
#                 if j + nums[j] >= i:
#                     dp[i] = min(dp[i],dp[j]+1)
#         print(dp)
#         return dp[length-1]

class Solution:
    # 动态规划 + 小贪心优化
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        # dp[i] 表示到小标i的点的最小步数
        dp = [inf for _ in range(length)]
        dp[0] = 0
    # 由于dp[]严格递增,直接找到最早能到第i个点的 j + nums[j]
        j = 0
        for i in range(1,length):
            while j + nums[j] < i:
                j += 1
            dp[i] = min(dp[i],dp[j]+1)
        print(dp)
        return dp[length-1]

class Solution:
    # 大贪心
    # 速度最快
    def jump(self, nums: List[int]) -> int:
        step = 0    # 返回的步数

        cur_pos = 0 # 当前能到的最大位置
        max_pos = 0 # 目前下标

        for i in range(len(nums)-1):
            max_pos = max(max_pos,i+nums[i])
            if i == cur_pos:
                cur_pos = max_pos
                step += 1

        return step

#小难理解
# https://leetcode.cn/problems/jump-game-ii/solutions/1703944/by-itcharge-xn4b/

fun = Solution()
print(fun.jump([1,2,1,1,1]))
