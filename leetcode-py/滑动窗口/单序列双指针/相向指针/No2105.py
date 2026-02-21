from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        res = 0
        left,right = 0,len(plants)-1
        c1,c2 = capacityA,capacityB
        while left < right:
            if c1 < plants[left]:
                c1 = capacityA
                res += 1
            c1 -= plants[left]
            if c2 < plants[right]:
                c2 = capacityB
                res += 1
            c2 -= plants[right]

            left += 1
            right -= 1

        if left == right:
            if c1 < plants[left] and c2 < plants[left]:
                res += 1
        return res  # 38ms
