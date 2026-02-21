from typing import List


class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        li = list(range(1, n + 1))
        total = sum(li)

        if total < target:
            return []
        

        for i in range(len(li) - 1, -1, -1):
            if total - li[i] * 2 < target:
                continue
            else:
                total -= li[i] * 2
                li[i] = -li[i]
            if total == target:
                break
        
        return sorted(li) if sum(li) == target else []

fun = Solution()
fun.lexSmallestNegatedPerm(1, 1)
