from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt = defaultdict(int)
        ans = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            temp = cnt.copy()
            for left in range(right + 1):
                if len(set(temp.values())) == 1:
                    ans = max(ans, right - left + 1)
                    break
                temp[s[left]] -= 1
                if temp[s[left]] == 0:
                    del temp[s[left]]
                if right - left + 1 < ans:
                    break
        return ans
    
fun = Solution()
fun.longestBalanced("zzabccy")