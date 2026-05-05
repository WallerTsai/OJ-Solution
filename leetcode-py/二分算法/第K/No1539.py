from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for x in arr:
            if x > k:
                return k
            k += 1
        return k




class Solution:
    # 二分
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        
        left, right = 0, len(arr)
        def check(i: int):
            if arr[i] - 1 - i >= k:
                return True
            else:
                return False
            
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return right + k    # logn