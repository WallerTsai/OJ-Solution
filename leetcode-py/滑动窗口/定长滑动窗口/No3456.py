from itertools import groupby


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for _,s in groupby(s):
            if len(list(s)) == k:
                return True
        else:
            return False




