from collections import defaultdict
from typing import List

MOD = 10 ** 9 + 7
class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans = left = 0
        count = defaultdict(int)
        for right, f in enumerate(flowers):
            count[f] += 1
            while count[f] > cnt:
                count[flowers[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans % MOD    # 162ms
