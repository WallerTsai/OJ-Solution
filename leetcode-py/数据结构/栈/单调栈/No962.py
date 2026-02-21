from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = left = 0
        for right,n in enumerate(nums):
            while left < right and n <= nums[left]:
                left += 1
            ans = max(ans,right-left)
        return ans # 错误
    

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return len(nums)
        ans = left = 0
        for right,n in enumerate(nums):
            if n >= nums[left]:
                ans = max(ans,right-left)
                left += 1
        return ans 

class Solution:
    # 暴力
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(0, n):
            for j in range(n - 1, i, -1):
                if nums[i] <= nums[j]:
                    ans = max(ans, j - i)
                    break
        return ans  # 超时

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        # 预处理,得到一个值严格单调递减的储存着下标的栈
        stack = []
        for i,n in enumerate(nums):
            if not stack or nums[stack[-1]] > n:
                stack.append(i)

        ans = 0
        j = len(nums) - 1
        while stack:
            while nums[j] < nums[stack[-1]]:
                j -= 1
            ans = max(ans,j - stack.pop())
        
        return ans # 55ms
    
fun = Solution()
print(fun.maxWidthRamp([6,0,8,2,1,5]))