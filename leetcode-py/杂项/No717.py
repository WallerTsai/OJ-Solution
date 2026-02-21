from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        last = None
        while i < n:
            if bits[i] == 1:
                i += 2
                last = 1
            else:
                i += 1
                last = 0
        
        return False if last else True



class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        left = 0
        while left < n - 1:
            if bits[left] == 0:
                left += 1
            else:
                left += 2
        return left == n - 1

