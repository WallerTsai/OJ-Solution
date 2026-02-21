from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        pre = 0
        for s in bank:
            n = s.count("1")
            ans += n * pre
            if n != 0:
                pre = n
        return ans



