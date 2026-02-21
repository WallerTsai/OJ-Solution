class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        ans = n = len(str(k))
        i = int("1" * n) % k
        while i:
            i = (i * 10 + 1) % k
            ans += 1
        return ans