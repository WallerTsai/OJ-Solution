from itertools import pairwise

# 堵车原理


class Solution:
    def maxOperations(self, s: str) -> int:
        a = s + "1" 
        ans = cnt1 = 0
        for ch1, ch2 in pairwise(a):
            if ch1 == "1": # pre == 1
                cnt1 += 1
            elif ch1 == "0" and ch2 == "1": # pre == 0 and cur == 1
                ans += cnt1
        return ans
    

class Solution:
    def maxOperations(self, s: str) -> int:
        ans = cnt1 = 0
        for i, c in enumerate(s):
            if c == '1':
                cnt1 += 1
            elif i > 0 and s[i - 1] == '1': # cur == 0 pre == 1
                ans += cnt1
        return ans


# 上面两种方法本质上都是边界处理