from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_num = pow(2, maximumBit) - 1
        cur_sum = 0
        ans = []
        for i in nums:
            cur_sum ^= i
            ans.append(cur_sum ^ max_num)
        return ans[::-1]    # 27ms