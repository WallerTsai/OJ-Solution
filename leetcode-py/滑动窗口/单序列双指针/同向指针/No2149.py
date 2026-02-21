from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        zhengshu = [x for x in nums if x > 0]
        fushu = [x for x in nums if x < 0]
        ans = []
        for z, f in zip(zhengshu,fushu):
            ans.extend([z,f])
        return ans  # 67ms

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i, j, ans = 0, 1, [0] * len(nums)
        for num in nums:
            if num > 0:
                ans[i] = num
                i += 2
            else:
                ans[j] = num
                j += 2
