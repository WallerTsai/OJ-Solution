from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        ans = 0
        li = []
        for a, b in zip(technique1, technique2):
            if a >= b:
                ans += a
                k -= 1
            else:
                ans += b
                li.append((a, b))

        if k > 0:
            li.sort(key=lambda x : x[1] - x[0])
            for a, b in li:
                ans += a - b
                k -= 1
                if k == 0:
                    break
        
        return ans  # 116ms


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        z = [(a, b) for a, b in zip(technique1, technique2)]
        z.sort(key=lambda x : x[1] - x[0])
        ans = 0
        for a, b in z:
            if k:
                ans += a
                k -= 1
                continue
            ans += a if a >= b else b
        return ans  # 279ms
    
class Solution:
    # 灵神
    def maxPoints(self, a: List[int], b: List[int], k: int) -> int:
        d = sorted((y - x for x, y in zip(a, b) if y > x), reverse=True)
        return sum(a) + sum(d[:len(a) - k])