from collections import defaultdict
from typing import Counter, List


class Solution:
    def check(self, d: dict, target: int) -> bool:
        if target == 0:
            return True
        for i, n in d.items():
            if i == 0:
                return True
            if n <= target:
                d[n] -= 1
                if self.check(d, target - n):
                    return True
        return False
                
                
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        cnt = Counter(nums)
        ans = []
        n = len(nums)
        for i in range(n, 0, -1):
            cnt[i] += cnt[i + 1]
            del cnt[i + 1]
            ans.append(self.check(cnt.copy(), k))

        return ans[::-1]    # 超时
    

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        n = len(nums)

        # 0-1背包
        # dp[i][j] 前i个硬币能否合成j
        dp = [[False] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i, num in enumerate(nums):
            for j in range(k + 1):
                if dp[i][j]:
                    dp[i + 1][j] = True
                elif j >= num and dp[i][j - num]:
                    dp[i + 1][j] = True

        # 指针i, 计数器count, 获取有多少个数 >= x
        i = n - 1
        count = 0

        ans = []
        ans.append(dp[-1][-1])

        # 限制多重背包
        for x in range(n - 1, 0, -1):
            # 更新count
            while i >= 0 and nums[i] >= x:
                count += 1
                i -= 1

            # conut 个 x 与 dp[n - count] 合并成一个背包
            temp = dp[n - count]    

            # 多重背包
            num = k
            flag = False
            for t in range(count + 1):
                if temp[num]:
                    # 可以合成
                    flag = True
                    break
                if num < x:
                    # 提前退出，没必要选了
                    break
                num -= x    # 选一个x
            ans.append(flag)

        return ans[::-1]    # 5385ms
    

class Solution:
    # 灵神
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()

        n = len(nums)
        ans = [False] * n
        f = [False] * (k + 1)
        f[0] = True  # 不选元素，和为 0

        i = 0
        for x in range(1, n + 1):
            # 增量地考虑所有恰好等于 x 的数
            # 小于 x 的数在之前的循环中已计算完毕，无需重复计算
            while i < n and nums[i] == x:
                for j in range(k, nums[i] - 1, -1):
                    f[j] = f[j] or f[j - nums[i]]  # 0-1 背包：不选 or 选
                i += 1

            # 枚举（从大于 x 的数中）选了 j 个 x
            for j in range(min(n - i, k // x) + 1):
                if f[k - j * x]:
                    ans[x - 1] = True
                    break
        return ans  # 1930ms