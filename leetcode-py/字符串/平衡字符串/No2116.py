class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        MAX = MIN = 0
        for c, lock in zip(s,locked):

            if lock == "1":
                k = 1 if c == "(" else -1
                MAX += k
                if MAX < 0:
                    return False
                MIN += k
            else:
                MAX += 1
                MIN -= 1

            if MIN < 0:
                MIN = 1
        return MIN == 0