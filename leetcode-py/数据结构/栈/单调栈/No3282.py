from itertools import pairwise
from typing import List


class Solution:
    # 单调栈
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        st = [0]
        for i, num in enumerate(nums):
            if num > nums[st[-1]]:
                st.append(i)

        if st[-1] != n - 1:
            st.append(n - 1)
        ans = 0
        for i, j in pairwise(st):
            ans += (j - i) * nums[i]
        return ans  # 59ms
    

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans = mx = 0
        for x in nums[:-1]:  # 也可以先 pop 掉最后一个数
            mx = max(mx, x)
            ans += mx
        return ans
