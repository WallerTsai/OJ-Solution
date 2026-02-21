from typing import List


class Solution:
    # 灵神
    # 很棒
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = pre_cnt = cnt = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i == len(nums) - 1 or x >= nums[i + 1]:  # i 是严格递增段的末尾
                ans = max(ans, cnt // 2, min(pre_cnt, cnt))
                pre_cnt = cnt
                cnt = 0
        return ans  # 1543ms
        
        
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        '''
        前后缀分解dp
        '''
        # left[i] 以 i 末尾最长严格递增子数组长度
        n = len(nums)
        left = [0] * n

        last = nums[0] - 1
        t = 0
        for i,num in enumerate(nums):
            if num > last:
                t += 1
            else:
                t = 1
            left[i] = t
            last = num

        # right[i] 同上，顺便枚举
        last = nums[-1] + 1
        t = 0
        res = 0
        for i in range(n-1,0,-1):
            if nums[i] < last:
                t += 1
            else:
                t = 1
            last = nums[i]
            
            res = max(res,min(left[i-1],t))

        return res  # 1644ms


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        ans = 1
        
        # 前缀
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1


        for i in range(1, n):
            ans = max(ans, dp[i] // 2, min(dp[i], dp[i - dp[i]]))
                
        return ans  # 1881ms
    
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = 1
        ans = 1
        
        # 前缀
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i + 1] = dp[i] + 1
            else:
                dp[i + 1] = 1


        for i in range(n):
            ans = max(ans, dp[i + 1] // 2, min(dp[i + 1], dp[i - dp[i + 1] + 1]))
                
        return ans


fun = Solution()
fun.maxIncreasingSubarrays([5,8,-2,-1])