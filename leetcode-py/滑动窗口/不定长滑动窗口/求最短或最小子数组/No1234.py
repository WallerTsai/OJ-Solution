from collections import defaultdict


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        res,left =len(s),0
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        if len(cnt) == 4 and min(cnt.values()) == n:
            return 0
        for right,c in enumerate(s):
            cnt[c] -= 1
            while left <= right and max(cnt.values()) <= n:
                res = min(res,right-left+1)
                cnt[s[left]] += 1
                left += 1
        return res  # 139ms
    
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        res,left =len(s),0

        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1

        if len(cnt) == 4 and min(cnt.values()) == n:
            return 0
        
        for right,c in enumerate(s):
            cnt[c] -= 1
            while left <= right and max(cnt.values()) <= n:
                res = min(res,right-left+1)
                cnt[s[left]] += 1
                left += 1
        return res


fun  = Solution()
out = fun.balancedString("WWEQERQWQWWRWWERQWEQ")