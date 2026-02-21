from collections import Counter
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        li = [nums[i] for i in range(1, len(nums)) if nums[i - 1] == key]
        cnt = Counter(li)
        return cnt.most_common(1)[0][0]