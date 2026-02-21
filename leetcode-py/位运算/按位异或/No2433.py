from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        cur = 0
        for num in pref:
            num ^= cur
            ans.append(num)
            cur ^= num
        return ans

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        cur = 0
        for num in pref:
            ans.append(cur ^ num)
            cur = num
        return ans

