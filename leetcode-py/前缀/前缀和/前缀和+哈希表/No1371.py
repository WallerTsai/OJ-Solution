# 前缀和 + 状态压缩

# 一个合理的字符串变化：aeiou --> aeioua -->aeiouae-->aeiouaea-->aeiouaeae
# 由此可见，从 aeiou 到 aeiouaeae 这个过程中，多余出来的 aeae 为符合条件的字符串
# 所以，在这个过程中，不管中间发生了什么样的变化，这两个状态之间对应的元音为偶数，也就是一定符合题意的字符串



class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        record = [-2] * 32 # 记录每个状态第一次出现的下标
        record[0] = -1
        pattern = 0 # 状态
        ans = 0
        for i in range(len(s)):

            if s[i] == 'a':
                pattern ^= (1<<0)
            elif s[i] == 'e':
                pattern ^= (1<<1)
            elif s[i] == 'i':
                pattern ^= (1<<2)
            elif s[i] == 'o':
                pattern ^= (1<<3)
            elif s[i] == 'u':
                pattern ^= (1<<4)

            if record[pattern] > -2:
                cur_length = i - record[pattern]
                ans = max(ans, cur_length)
            else:
                record[pattern] = i

        return ans

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        seen = {0: -1}
        state = 0
        res = 0
        for i, c in enumerate(s):
            if c in vowel:
                state ^= vowel[c]
            if state in seen:
                res = max(res, i - seen[state])
            else:
                seen[state] = i
        return res

f = Solution()
f.findTheLongestSubstring("eleetminicoworoep")

