from typing import List
# 1 2 1 3 3
# 1 1 2 3 2

# 1 2 3
# 1 2 3 
# 1 2 3

class Solution:
    # LC 300 改
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x >= y:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return dp
    
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        dps = []
        for s in strs:
            nums = [ord(ch) - ord('a') for ch in s]
            dps.append(self.lengthOfLIS(nums))

        delete_set = set()
        for dp in dps:
            cur_max = max(dp)
            for i in range(m - 1, -1, -1):
                x = dp[i]
                if x < cur_max:
                    delete_set.add(i)
                elif x == cur_max:
                    cur_max -= 1

        ans = 0
        for dp in dps:
            delete_num = 0
            cur_x = 1
            for i, x in enumerate(dp):
                if i in delete_set:
                    continue

                if x == cur_x:
                    cur_x += 1
                elif x < cur_x:
                    delete_num += 1
    
            ans = max(ans, delete_num)

        return ans + len(delete_set)    # 错误 ["aaababa","ababbaa"] 预期4 输出3
    
fun = Solution()
fun.minDeletionSize(["aaababa","ababbaa"])


class Solution:
    # 灵神
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        f = [0] * m
        for i in range(m):
            for j in range(i):
                # 如果 f[j] <= f[i]，就不用跑 O(n) 的 all 了
                if f[j] > f[i] and all(s[j] <= s[i] for s in strs):
                    f[i] = f[j]
            f[i] += 1
        return m - max(f)
