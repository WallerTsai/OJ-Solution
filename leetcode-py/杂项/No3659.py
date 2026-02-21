from typing import Counter, List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        
        length = n // k
        cnt = Counter(nums)
        for i in cnt.values():
            if i > length:
                return False
        
        return True
    
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        mx = max(Counter(nums).values())
        return mx * k <= n