# 新出生的兔子需要delay天成熟，然后成熟之后（包括当天）每天开始生新兔子，
# 直到forget-1天后死亡，求问最后一天还存活多少个兔子？

MOD  = 10 ** 9 + 7
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        cnt = [0] * (forget)
        cnt[0] = 1
        for i in range(n - 1):
            cnt[-1] = 0
            new = 0
            for j in range(forget - 2, -1, -1):
                if j >= delay - 1:
                    new += cnt[j]
                cnt[j + 1] = cnt[j] 
            cnt[0] = new % MOD

        return sum(cnt) % MOD   # 675ms
    
"""以下摘自灵神题解"""
# https://leetcode.cn/problems/number-of-people-aware-of-a-secret/solutions/1641511/by-endlesscheng-2x0z/
# 方法一：刷表法（用当前状态更新其它状态）
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        f = [0] * n # 第 i 天
        f[0] = 1
        cnt_b = 0
        for i, v in enumerate(f):
            if i + delay >= n:
                cnt_b += v
            for j in range(i + delay, min(i + forget, n)):
                f[j] = (f[j] + v) % MOD
        return (f[-1] + cnt_b) % MOD
# 差分优化
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        diff = [0] * n
        diff[0] = 1  # f[0] = 1，相当于 diff[0] = 1, diff[1] = -1
        diff[1] = -1
        f = cnt_b = 0
        for i, d in enumerate(diff):
            f = (f + d) % MOD
            if i + delay >= n:
                cnt_b += f
            else:
                diff[i + delay] += f
                if i + forget < n:
                    diff[i + forget] -= f
        return (f + cnt_b) % MOD    # 5ms
    
# 方法二：填表法（用其它状态计算当前状态）
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        sum = [0] * (n + 1)
        sum[1] = 1
        for i in range(2, n + 1):
            f = sum[max(i - delay, 0)] - sum[max(i - forget, 0)]
            sum[i] = (sum[i - 1] + f) % MOD
        return (sum[n] - sum[max(n - forget, 0)]) % MOD
    
fun = Solution()
fun.peopleAwareOfSecret(6, 2, 4)