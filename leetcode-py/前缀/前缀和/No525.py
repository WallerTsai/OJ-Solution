from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 1.将 0 看成 -1
        # 2.利用哈希表，记录前缀和出现的下标
        cnt = defaultdict(int)
        cnt[0] = -1
        ans = cur = 0
        for i, n in enumerate(nums):
            if n == 1:
                cur += 1
            else:
                cur -= 1
            if cur not in cnt:
                cnt[cur] = i
            else:
                ans = max(ans,i - cnt[cur])
        return ans  # 107ms


