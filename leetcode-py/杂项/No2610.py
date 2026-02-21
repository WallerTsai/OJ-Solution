from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        ans = []
        while cnt:
            path = []
            for k in cnt.keys():
                path.append(k)
                cnt[k] -= 1
                if cnt[k] == 0:
                    cnt.pop(k)
            ans.append(path[:])
        return ans
    
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        ans = []
        while cnt:
            path = []
            for k in list(cnt.keys()):
                path.append(k)
                cnt[k] -= 1
                if cnt[k] == 0:
                    cnt.pop(k)
            ans.append(path[:])
        return ans