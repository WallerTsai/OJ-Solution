from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n1 = len(v1)
        n2 = len(v2)
        if n1 < n2:
            v1.extend([0] * (n2 - n1))
        else:
            v2.extend([0] * (n1 - n2))
        
        for i1, i2 in zip(v1, v2):
            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1
            
        return 0
    
class Solution:
    # leetcode 官方
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0