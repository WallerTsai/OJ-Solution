from typing import List


class Solution:
    # 枚举元素的奇偶性
    def maximumLength(self, nums: List[int]) -> int:
        ans = 0
        for pattern in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            # 分别表示 全偶， 偶奇交替， 奇偶交替， 全奇
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            ans = max(ans, cnt)
        return ans # 131ms
    
class Solution:
    # 动态规划
    # 只有四种情况：
    # 偶数位奇偶性为偶，奇数位奇偶性为偶
    # 偶数位奇偶性为偶，奇数位奇偶性为奇
    # 偶数位奇偶性为奇，奇数位奇偶性为偶
    # 偶数位奇偶性为奇，奇数位奇偶性为奇
    def maximumLength(self, nums: List[int]) -> int:
        dp = [0] * 4 # 一共四种情况
        for num in nums:
            cur = num % 2
            for i in range(4):
                if (i >> (dp[i] % 2)) & 1 == cur:   # 很巧妙
                    # 通过位运算判断四种情况当前位置
                    dp[i] += 1
        return max(dp)  # 235ms
    
class Solution:
    # 灵神
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        f = [[0] * k for _ in range(k)]
        for x in nums:
            x %= k
            for y, fxy in enumerate(f[x]):
                f[y][x] = fxy + 1
        return max(map(max, f)) # 118ms