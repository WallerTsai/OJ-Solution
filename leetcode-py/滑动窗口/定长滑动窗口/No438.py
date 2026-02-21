from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        cnt1 = Counter(p)
        cnt2 = Counter()
        left = 0
        ans = []

        for i, ch in enumerate(s):
            cnt2[ch] += 1

            
            if i >= n:
                cnt2[s[left]] -= 1
                if cnt2[s[left]] == 0:
                    del cnt2[s[left]]
                left += 1

            if cnt1 == cnt2:
                ans.append(left)
            
        return ans
    
class Solution:
    # 不定长滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans
    
fun = Solution()
fun.findAnagrams("abab", "ab")