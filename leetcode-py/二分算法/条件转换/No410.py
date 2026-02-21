from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(limit):
            m = count = 0
            for x in nums:
                if count + x <= limit:
                    count += x
                else:
                    m += 1
                    count = x
            if count:
                m += 1
            return m <= k
        
        left, right = nums[0], sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left



