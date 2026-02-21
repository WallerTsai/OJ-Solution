from collections import defaultdict
from itertools import accumulate
from typing import List


# (s[r] - s[l]) mod modulo = k mod modulo
# -> (s[r] - k) mod modulo = s[l] mod modulo
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        pre_sum = list(accumulate((x % modulo == k for x in nums), initial=0))
        cnt = defaultdict(int)
        ans = 0
        for i in pre_sum:
            if i >= k:
                ans += cnt[(i - k) % modulo]
            cnt[i % modulo] += 1
        return ans


