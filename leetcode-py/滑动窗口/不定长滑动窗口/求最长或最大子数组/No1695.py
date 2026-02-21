from collections import deque
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = temp = left = 0
        for right,num in enumerate(nums):
            temp += num
            while num in nums[left:right]:
                temp -= nums[left]
                left += 1
            res = max(res,temp)
        return res  # 超时
    
class Solution:
    # 双队列
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = temp = 0
        q = deque()
        for num in nums:
            temp += num
            while num in q:
                temp -= q.popleft()
            q.append(num)
            res = max(res,temp)
        return res  # 8823ms 太慢了

class Solution:
    # 利用集合居然这么快
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = temp = left = 0
        the_set = set()
        for right,num in enumerate(nums):
            temp += num
            while num in the_set:
                temp -= nums[left]
                the_set.remove(nums[left])
                left += 1
            the_set.add(num)
            res = max(res,temp)
        return res  # 215ms

class Solution:
    def maximumUniqueSubarray(self, nums):
        MAXN = 10005
        m = [0] * MAXN
        left = 0
        n = len(nums)
        ans = 0
        sum_ = 0

        for right in range(n):
            m[nums[right]] += 1
            sum_ += nums[right]
            while m[nums[right]] > 1:
                m[nums[left]] -= 1
                sum_ -= nums[left]
                left += 1
            ans = max(ans, sum_)