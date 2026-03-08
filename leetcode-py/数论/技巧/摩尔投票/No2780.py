from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = hp = 0
        for x in nums:
            if hp == 0:  # x 是初始擂主，生命值为 1
                ans, hp = x, 1
            else:  # 比武，同门加血，否则扣血
                hp += 1 if x == ans else -1
        return ans
    
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        t = self.majorityElement(nums)
        right = nums.count(t)
        left = 0
        for i, x in enumerate(nums):
            if x == t:
                left += 1
                right -= 1
            if left > (i + 1) // 2 and right > (n - i - 1) // 2:
                return i
        return -1 

        