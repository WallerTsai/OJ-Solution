from collections import defaultdict
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        cnt[0] = 1
        pre_mod = nums[0]
        for i in nums[1:]:
            pre_mod = (pre_mod + i) % k
            if cnt[pre_mod] > 0:
                return True
            cnt[pre_mod] += 1
        return False


class Solution:
    # 延迟添加
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        pre_mod = 0
        cur_mod = 0
        for i in nums:
            cur_mod = (cur_mod + i) % k
            if cnt[cur_mod] > 0:
                return True
            cnt[pre_mod] += 1
            pre_mod = cur_mod
        return False
    
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d=set()
        s=0
        for x in nums:
            tmp=s
            s=(s+x)%k
            if s in d:
                return True
            d.add(tmp)
        return False