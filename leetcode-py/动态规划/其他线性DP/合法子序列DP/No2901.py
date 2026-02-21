from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def check(s: str, t: str) -> bool:
            return len(s) == len(t) and sum( x != y for x, y in zip(s, t)) == 1
        
        n = len(groups)
        f = [1] * n # 以 i 结尾的最长子序列
        from_ = [-1] * n
        max_i = 0
        
        for i, x in enumerate(groups):
            for j, y in enumerate(groups[:i]):
                if x != y and f[i] < f[j] + 1 and check(words[i], words[j]):
                    f[i] = f[j] + 1
                    from_[i] = j
                    if f[i] > f[max_i]:
                        max_i = i

        ans = []
        i = max_i
        for _ in range(f[max_i]):
            ans.append(words[i])
            i = from_[i]

        return ans[::-1]    # 1721ms