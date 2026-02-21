class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 1
        left = same = 0
        for right in range(1,len(s)):
            same += (s[right]==s[right-1])
            if same > 1:
                left += 1
                while s[left] != s[left-1]:
                    left += 1
                same -= 1
            res = max(res,right-left+1)
        return res  # 24ms
    
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 1
        left = same = 0
        next_index = 0
        for right in range(1,len(s)):
            if s[right] == s[right-1]:
                same += 1
                
                if same > 1:
                    left = next_index
                    same -= 1
                
                next_index = right

            res = max(res,right-left+1)
        return res  # 8ms

class Solution:
    # leetcode最快
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = pos = 0
        ans = 1
        for right in range(1,len(s)):
            if s[right] == s[right - 1]:
                left = pos
                pos = right
            ans = max(ans,right - left + 1)
        return ans
