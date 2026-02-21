from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        l = 1
        index_set = set()
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                l += 1
            else:
                l = 1
            if l >= k:
                if (i - k) in index_set:
                    return True
                index_set.add(i)
        return False


class Solution:
    # 灵神
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        ans = pre_cnt = cnt = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i == len(nums) - 1 or x >= nums[i + 1]:  # i 是严格递增段的末尾
                ans = max(ans, cnt // 2, min(pre_cnt, cnt))
                pre_cnt = cnt
                cnt = 0
        return ans >= k


class Solution:
    # wxyz
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # dp[i] 表示以 nums[i] 结尾的连续递增子数组的长度
        dp = [0] * n
        dp[0] = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1

        # 遍历寻找满足条件的相邻点
        for i in range(2 * k - 1, n):
            # 检查以 i-k 结尾的第一个子数组长度是否满足
            len_first = dp[i - k]
            # 检查以 i 结尾的第二个子数组长度是否满足
            len_second = dp[i]
            
            if len_first >= k and len_second >= k:
                return True
                
        return False

