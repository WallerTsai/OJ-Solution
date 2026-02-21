from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res =  0
        left = 0
        cnt = 0
        for right,num in enumerate(nums):
            if num == 0:
                cnt += 1
            
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1

            if cnt == k:
                res = max(res,right-left+1)

        if right-left+1 == len(nums):
            return len(nums)
        
        return res  # 51ms

class Solution:
    # leetcode最快
    # 窗口长度减小是没有必要的
    # 每次只移一位,即保证窗口一直不变小
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1


