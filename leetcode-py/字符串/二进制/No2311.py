class Solution:
    # 贪心
    def longestSubsequence(self, s: str, k: int) -> int:
        cnt0 = 0
        for i,ch in enumerate(s):
            if ch == "0":
                cnt0 += 1
            else:
                temp = "0" * cnt0 + s[i:]
                if int(temp,2) <= k:
                    return len(temp)
        return cnt0 # 31ms
    
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n, m = len(s), k.bit_length()
        if n < m:  # int(s, 2) < k
            return n  # 全选
        ans = m if int(s[-m:], 2) <= k else m - 1  # 后缀长度
        return ans + s[:-m].count('0')  # 添加前导零    # 0ms