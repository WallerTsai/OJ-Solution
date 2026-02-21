from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        suf_total = sum(nums)
        ans = pre_total = 0
        for i, num in enumerate(nums):
            if num == 0:
                if pre_total == suf_total:
                    ans += 2
                elif abs(pre_total - suf_total) == 1:
                    ans += 1
            else:
                pre_total += num
                suf_total -= num
        return ans
    
    
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        pre = 0
        res = 0
        for i in nums:
            if i:
                pre += i
            else:
                res += max(0,2-abs(total-2*pre))
        return res    