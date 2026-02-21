from collections import Counter, defaultdict
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        pre_cnt = defaultdict(int)
        suf_cnt = Counter(nums)
        ans = 0
        for num in nums:
            suf_cnt[num] -= 1
            x = num * 2
            if pre_cnt[x] and suf_cnt[x]:
                ans = (ans +  pre_cnt[x] * suf_cnt[x]) % MOD
            pre_cnt[num] += 1
        return ans  # 826ms


class Solution:
    # 灵神
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        cnt1 = defaultdict(int)
        cnt12 = defaultdict(int)
        cnt123 = 0
        for x in nums:
            if x % 2 == 0:
                cnt123 += cnt12[x // 2]  # 把 x 当作 nums[k]
            cnt12[x] += cnt1[x * 2]  # 把 x 当作 nums[j]
            cnt1[x] += 1  # 把 x 当作 nums[i]
        return cnt123 % MOD