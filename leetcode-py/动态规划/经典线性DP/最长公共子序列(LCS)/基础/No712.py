
from collections import Counter

fmax = lambda x, y : x if x > y else y
fmin = lambda x, y : x if x < y else y
class Solution:
    # 暴力
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        cnt1 = Counter(s1)
        cnt2 = Counter(s2)

        ans = 0
        cnt1.subtract(cnt2)

        for ch, n in cnt1.items():
            ans += ord(ch) * abs(n)

        return ans  # 错误 注意顺序
    

class Solution:
    # 正难则反
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        total = sum(ord(ch) for ch in s1) + sum(ord(ch) for ch in s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + ord(x)
                else:
                    dp[i + 1][j + 1] = fmax(dp[i][j + 1], dp[i + 1][j])
        
        return total - dp[n][m] * 2 # 195ms



class Solution:
    # 空间优化
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s2)
        total = sum(map(ord, s1)) + sum(map(ord, s2))

        f = [0] * (m + 1)
        for x in s1:
            ord_x = ord(x)
            pre = 0  # f[0]
            for j, y in enumerate(s2):
                tmp = f[j + 1]
                if x == y:
                    f[j + 1] = pre + ord_x
                else:
                    f[j + 1] = max(f[j + 1], f[j])
                pre = tmp
        return total - f[m] * 2