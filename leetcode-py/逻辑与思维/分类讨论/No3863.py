class Solution:
    def minOperations(self, s: str) -> int:
        li = list(s)
        MAX, MIN = max(li), min(li)
        n = len(li)

        if li == sorted(li):
            return 0
        
        if n == 2:
            return -1
        
        if li[-1] == MAX or li[0] == MIN:
            return 1
        
        if li[0] == MAX and li[-1] == MIN and li.count(MAX) == 1 and li.count(MIN) == 1:
            return 3
        
        return 2