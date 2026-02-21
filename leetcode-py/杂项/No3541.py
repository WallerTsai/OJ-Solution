class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = [0] * 26
        max_vowel_cnt = max_consonant_cnt = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            cnt[idx] += 1
            if ch in "aeiou":
                max_vowel_cnt = max(max_vowel_cnt, cnt[idx])
            else:
                max_consonant_cnt = max(max_consonant_cnt, cnt[idx])
        return max_vowel_cnt + max_consonant_cnt
    
class Solution:
    # 灵神
    # 位运算优化
    # 我们可以把元音集合{a,e,i,o,u}
    # 视作数字 2^0 +2^4 +2^8 +2^14 +2^20 = 1065233
    # 即十六进制的 0x104111。

    def maxFreqSum(self, s: str) -> int:
        VOWEL_MASK = 0x104111
        cnt = [0] * 26
        max_cnt = [0] * 2
        for ch in s:
            ch = ord(ch) - ord('a')
            bit = VOWEL_MASK >> ch & 1
            cnt[ch] += 1
            max_cnt[bit] = max(max_cnt[bit], cnt[ch])
        return sum(max_cnt)