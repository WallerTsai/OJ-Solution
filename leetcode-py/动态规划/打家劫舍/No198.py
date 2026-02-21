from typing import List
#b站up灵茶山艾府学习视频https://www.bilibili.com/video/BV1Xj411K7oF/?spm_id_from=333.999.0.0&vd_source=de36bd0fcb6e28e6957655da8defde06

# class Solution:
#     #递归
#     def rob(self, nums: List[int]) -> int:
#         length = len(nums)
#         def dfs(n):
#             if n < 0:
#                 return 0
#             res = max(dfs(n-1),dfs(n-2) + nums[n])
#             return res
#         return dfs(length-1)
#     #超出时间限制
    
# class Solution:
#     #递归 + cache优化
#     def rob(self, nums: List[int]) -> int:
#         length = len(nums)
#         cache = [-1] * length
#         def dfs(n):
#             if n < 0:
#                 return 0
#             if cache[n] !=-1:
#                 return cache[n]
#             res = max(dfs(n-1),dfs(n-2) + nums[n])
#             cache[n] = res
#             return res
#         return dfs(length-1)
    
# class Solution:
#     #动态规划
#     def rob(self, nums: List[int]) -> int:
#         length = len(nums)

#         if length == 1:
#             return nums[0]
#         if length == 2:
#             return max(nums[0],nums[1])
        
#         # up的巧妙写法
#         # dp = [0] * (length+2)
#         # for i,x in enumerate(nums):
#         #     dp[i+2] = max(dp[i+1],dp[i]+x)
#         # return dp[-1]
        
#         dp = [0] * length
#         dp[0] = nums[0]
#         dp[1] = max(nums[0],nums[1])
#         for i in range(2,length):
#             dp[i] = max(dp[i-1],dp[i-2]+nums[i])
#         return dp[-1]
#     #内存消耗太大

class Solution:
    #动态规划
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0],nums[1])
        
        # up的巧妙写法
        # dp = [0] * (length+2)
        # for i,x in enumerate(nums):
        #     dp[i+2] = max(dp[i+1],dp[i]+x)
        # return dp[-1]
        
        dp = [0] * length
        a = nums[0]
        b = max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(b,a+nums[i])
            a = b
            b = dp[i]
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1

if __name__ == "__main__":
    fun = Solution()
    nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    outcome = fun.rob(nums)
    print(outcome)

