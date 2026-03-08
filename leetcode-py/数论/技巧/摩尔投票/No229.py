from collections import defaultdict
from typing import List

def majorityElement_k(nums: List[int], k: int) -> list[int]:
    n = len(nums)
    if n == 0 or k < 2:
        return []

    candidates = {} 
    for num in nums:
        if num in candidates:
            candidates[num] += 1
        elif len(candidates) < k - 1:
            candidates[num] = 1
        else:
            for key in list(candidates.keys()):
                candidates[key] -= 1
                if candidates[key] == 0:
                    del candidates[key]

    result = set()
    counts = defaultdict(int)
    for num in nums:
        if num in candidates:
            counts[num] += 1
            if counts[num] > n // k:
                result.add(num)

    return list(result)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return majorityElement_k(nums, 3)