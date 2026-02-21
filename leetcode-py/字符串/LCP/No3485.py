from typing import List


class Solution:
    # 灵神
    def lcp(self, s: str, t: str) -> int:
        for i, (x,y) in enumerate(zip(s,t)):
            if x != y:
                return i
        return min(len(s), len(t))
    
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)

        if k == n:
            return [0] * n
        
        index = list(range(n))
        index.sort(key=lambda i : words[i])

        mx = mx2 = mx_i = -1
        for i in range(n-k+1):
            lcp = self.lcp(words[index[i]],words[index[i+k-1]])
            if lcp > mx:
                mx, mx2, mx_i = lcp, mx, i
            elif lcp > mx2:
                mx2 = lcp

        ans = [mx] * n

        for i in index[mx_i: mx_i+k]:
            ans[i] = mx2

        return ans 