from collections import Counter, defaultdict
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = -1 # 去掉空集
        path = []
        def dfs(i:int)->int:
            if i == n:
                nonlocal ans 
                ans += 1
                return

            dfs(i+1)
            if not ((nums[i] - k) in path or (nums[i] + k) in path):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans  # 995ms
    
class Solution:
    # 灵神
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = defaultdict(int)

        # nums[i] 选或不选
        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1
                return
            dfs(i + 1)  # 不选
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:  # 可以选
                cnt[x] += 1  # 选
                dfs(i + 1)  # 讨论 nums[i+1] 选或不选
                cnt[x] -= 1  # 撤销，恢复现场

        dfs(0)
        return ans

class Solution:
    # 灵神，递推
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        for x in nums:
            # 模 k 同余的数分到同一组，记录元素 x 及其出现次数
            groups[x % k][x] += 1

        ans = 1
        for cnt in groups.values():
            # 计算这一组的方案数
            a = sorted(cnt.items())
            m = len(a)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 1 << a[0][1]
            for i in range(1, m):
                if a[i][0] - a[i - 1][0] == k:
                    f[i + 1] = f[i] + f[i - 1] * ((1 << a[i][1]) - 1)
                else:
                    f[i + 1] = f[i] << a[i][1]
            ans *= f[m]  # 每组方案数相乘
        return ans - 1  # 去掉空集
    


