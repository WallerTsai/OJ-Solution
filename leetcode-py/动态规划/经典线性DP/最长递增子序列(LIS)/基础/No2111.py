from bisect import bisect_right
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(k):
            li = []
            for j in range(i, n, k):
                idx =  bisect_right(li, arr[j])
                if idx == len(li):
                    li.append(arr[j])
                else:
                    li[idx] = arr[j]
                    ans += 1
        return ans