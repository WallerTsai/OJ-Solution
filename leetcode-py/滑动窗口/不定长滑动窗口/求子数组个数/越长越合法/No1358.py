class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {
            'a':0,
            'b':0,
            'c':0
        }
        res = left = 0
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt['a'] >= 1 and cnt['b'] >= 1 and cnt['c'] >= 1:
                res += len(s) - right
                cnt[s[left]] -= 1
                left += 1
        return res  # 127ms

class Solution:
    # leetcode 大佬
    # 太绝了这代码
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        left = [-1] * 3

        for right, ele in enumerate(s):
            left[ord(ele) - 97] = right
            ans += min(left) + 1
        
        return ans
    
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {
            'a':0,
            'b':0,
            'c':0
        }
        res = left = 0
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt['a'] >= 1 and cnt['b'] >= 1 and cnt['c'] >= 1:
                cnt[s[left]] -= 1
                left += 1
            res += left
        return res