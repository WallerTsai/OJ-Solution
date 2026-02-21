from typing import List


class Solution:
    # 类似于接雨水
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            if left[i] != -1 and right[i] != n:
                ans += 1

        return ans
    
class Solution:
    # 灵神
    def bowlSubarrays(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for i, x in enumerate(nums):
            while st and nums[st[-1]] < x:
                # j=st[-1] 右侧严格大于 nums[j] 的数的下标是 i
                if i - st.pop() > 1:  # 子数组的长度至少为 3
                    ans += 1
            # i 左侧大于等于 nums[i] 的数的下标是 st[-1]
            if st and i - st[-1] > 1:  # 子数组的长度至少为 3
                ans += 1
            st.append(i)
        return ans

