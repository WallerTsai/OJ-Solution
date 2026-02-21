from typing import List
# 状态机解法

class Solution:
    def numOfSubsequences(self, s: str) -> int:
        s = "#" + s + "#"
        n = len(s)

        pre_L = [0] * n
        suf_CT = [0] * n
        suf_T = [0] * n

        for i in range(n - 2, -1, -1):
            if s[i] == "T":
                suf_T[i] = suf_T[i + 1] + 1
            else:
                suf_T[i] = suf_T[i + 1]

            if s[i] == "C":
                suf_CT[i] = suf_CT[i + 1] + suf_T[i + 1]
            else:
                suf_CT[i] = suf_CT[i + 1]
        
        ans = max_increase = pre_LC = 0
        # 规定新加的字母在现在遍历的字母后面
        for i in range(n - 1):
            ch = s[i]

            if ch == 'L':
                pre_L[i] = pre_L[i - 1] + 1

                ans += suf_CT[i + 1]

            else:
                pre_L[i] = pre_L[i - 1]

            if ch == 'C':
                pre_LC += pre_L[i]

            max_increase = max(max_increase, suf_CT[i + 1], pre_L[i] * suf_T[i + 1], pre_LC)
                
        
        return ans + max_increase   # 703ms


class Solution:
    # 状态机DP
    def numOfSubsequences(self, s: str) -> int:
        cnt_t = s.count("T")
        cnt_l = cnt_lc = cnt_lct = cnt_c = cnt_ct = cnt_lt = 0
        # 如果添加 L 贪心的想 肯定添加在最左边 ans += cnt_ct(随遍历单调增)
        # 如果添加 T 贪心的想 肯定添加在最右边 ans += cnt_lc(随遍历单调增)
        # 如果添加 C 则需要遍历找 cnt_lt 最大值
        for ch in s:
            
            if ch == "L":
                cnt_l += 1
            elif ch == "C":
                cnt_lc += cnt_l
                cnt_c += 1
            elif ch == "T":
                cnt_lct += cnt_lc
                cnt_ct += cnt_c
                cnt_t -= 1

            cnt_lt = max(cnt_lt, cnt_l * cnt_t)

        return cnt_lct + max(cnt_lc, cnt_ct, cnt_lt)    # 235ms

fun = Solution()
fun.numOfSubsequences("LCCT")
