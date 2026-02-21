class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for _ in range(1,n):
            start += 2
            res ^= start
        return res
    

# 异或性质
# 1) 0 ^ x = x
# 2) x ^ x = 0
# 3) 2x ^ (2x+1) = 1


