from collections import Counter, defaultdict
from string import ascii_lowercase


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        idx = [-1] * 26
        cnt = [0] * 26
        for i, ch in enumerate(s):
            if cnt[ord(ch) - ord('a')] == 0:
                cnt[ord(ch) - ord('a')] += 1
                idx[ord(ch) - ord('a')] = i
            else:
                ans += i - idx[ord(ch) - ord('a')] - 1

        return ans  # 错误要去重

# 以下均是灵神题解


class Solution:
    # 字符串find方法
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for alpha in ascii_lowercase:  # 枚举两侧字母 alpha
            i = s.find(alpha)  # 最左边的 alpha 的下标
            if i < 0:  # s 中没有 alpha
                continue
            j = s.rfind(alpha)  # 最右边的 alpha 的下标
            ans += len(set(s[i + 1: j]))  # 统计有多少个不同的中间字母
        return ans  # 91ms
    

class Solution:
    # 前后缀分解
    def countPalindromicSubsequence(self, s: str) -> int:
        suf_cnt = Counter(s[1:])  # 统计 [1,n-1] 每个字母的个数
        pre_set = set()
        st = set()
        for i in range(1, len(s) - 1):  # 枚举中间字母 mid
            mid = s[i]
            suf_cnt[mid] -= 1  # 撤销 mid 的计数，suf_cnt 剩下的就是后缀 [i+1,n-1] 每个字母的个数
            if suf_cnt[mid] == 0:  # 后缀 [i+1,n-1] 不包含 mid
                del suf_cnt[mid]  # 从 suf_cnt 中去掉 mid
            pre_set.add(s[i - 1])  # 记录前缀 [0,i-1] 有哪些字母
            for alpha in pre_set & suf_cnt.keys():  # mid 的左右两侧都有字母 alpha
                st.add(alpha + mid)
        return len(st) 
    

class Solution:
    # 前后缀分解 + 位运算
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ord_a = ord('a')

        # 统计 [1,n-1] 每个字母的个数
        suf_cnt = [0] * 26
        suf = 0
        for ch in s[1:]:
            ch = ord(ch) - ord_a
            suf_cnt[ch] += 1
            suf |= 1 << ch  # 把 ch 记录到二进制数 suf 中，表示后缀有 ch

        pre = 0
        ans = [0] * 26  # ans[mid] = 由 alpha 组成的二进制数
        for i in range(1, n - 1):  # 枚举中间字母 mid
            mid = ord(s[i]) - ord_a
            suf_cnt[mid] -= 1  # 撤销 mid 的计数，suf_cnt 剩下的就是后缀 [i+1,n-1] 每个字母的个数
            if suf_cnt[mid] == 0:  # 后缀 [i+1,n-1] 不包含 mid
                suf ^= 1 << mid  # 从 suf 中去掉 mid
            pre |= 1 << (ord(s[i - 1]) - ord_a)  # 把 s[i-1] 记录到二进制数 pre 中，表示前缀有 s[i-1]
            ans[mid] |= pre & suf  # 计算 pre 和 suf 的交集，|= 表示把交集中的字母加到 ans[mid] 中

        return sum(mask.bit_count() for mask in ans)  # mask 中的每个 1 对应着一个 alpha    # 274ms