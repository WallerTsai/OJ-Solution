from collections import Counter
from functools import cache
from typing import List




class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=len)

        cnts = []
        for str in strs:
            temp = Counter(str)
            cnts.append((temp['0'], temp['1']))

        ans =  0
        path = []
        
        def dfs(i: int, sum_zero: int, sum_one):
            if i == len(strs):
                return

            cnt = cnts[i]
            if sum_zero + cnt[0] <= m and sum_one + cnt[1] <= n:
                # 选
                path.append(i)
                nonlocal ans
                if len(path) > ans:
                    ans = len(path)
                dfs(i + 1, sum_zero + cnt[0], sum_one + cnt[1])
                # 不选
                path.pop()
            dfs(i + 1, sum_zero, sum_one)

        dfs(0, 0, 0)
        return ans  # 超时 25 / 77
    

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            cnts.append((temp['0'], temp['1']))

        ans =  0
        path = []
        
        def dfs(i: int, sum_zero: int, sum_one):

            if sum_zero <= m and sum_one <= n:
                nonlocal ans
                ans = max(ans, len(path))
            else:
                return
            
            if i == len(strs):
                return
            if len(path) + len(strs) - i <= ans:
                return
            
            cnt = cnts[i]
            # 选
            path.append(i)
            dfs(i + 1, sum_zero + cnt[0], sum_one + cnt[1])
            # 不选
            path.pop()
            dfs(i + 1, sum_zero, sum_one)

        dfs(0, 0, 0)
        return ans  # 超时 57 / 77
    

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            if temp['0'] > m or temp['1'] > n:
                continue
            cnts.append((temp['0'], temp['1']))

        ans =  0
        path = []
        lenght = len(cnts)
        
        def dfs(i: int, sum_zero: int, sum_one):

            if sum_zero <= m and sum_one <= n:
                nonlocal ans
                ans = max(ans, len(path))
            else:
                return
            
            if i == lenght:
                return
            if len(path) + lenght - i <= ans:
                return
            
            cnt = cnts[i]
            # 选
            path.append(i)
            dfs(i + 1, sum_zero + cnt[0], sum_one + cnt[1])
            # 不选
            path.pop()
            dfs(i + 1, sum_zero, sum_one)

        dfs(0, 0, 0)
        return ans  # 超时 57 / 77
    


# 因为只要记录个数，考虑 DP

class Solution:
    # dfs
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            if temp['0'] > m or temp['1'] > n:
                continue
            cnts.append((temp['0'], temp['1']))

        lenght = len(cnts)

        @cache
        def dfs(i: int, zero: int, one: int) -> int:
            if i < 0:
                return 0
            # 不选
            res = dfs(i - 1, zero, one)
            
            # 选
            x = cnts[i]
            if x[0] <= zero and x[1] <= one:
                res = max(res, dfs(i - 1, zero - x[0], one - x[1]) + 1)
            return res
        
        return dfs(lenght - 1, m, n)    # 1347ms

class Solution:
    # 递推
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            if temp['0'] > m or temp['1'] > n:
                continue
            cnts.append((temp['0'], temp['1']))

        lenght = len(cnts)

        dp = [[[0] * (n + 1) for _ in range(m +  1)] for _ in range(lenght + 1)]
        for i, x in enumerate(cnts):
            zero_num, one_num = x[0], x[1]
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zero_num and k >= one_num:
                        dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - zero_num][k - one_num] + 1)
                    else:
                        dp[i + 1][j][k] = dp[i][j][k]
        
        return dp[lenght][m][n] # 2219ms
    

class Solution:
    # 递推 + 空间优化
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            if temp['0'] > m or temp['1'] > n:
                continue
            cnts.append((temp['0'], temp['1']))

        dp = [[0] * (n + 1) for _ in range(m +  1)]
        for x in cnts:
            zero_num, one_num = x[0], x[1]
            for j in range(m, zero_num - 1, -1):
                for k in range(n, one_num - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zero_num][k - one_num] + 1)
                    
        return dp[m][n] # 1653ms
    
class Solution:
    # 递推 + 空间优化 + 循环优化
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            if temp['0'] > m or temp['1'] > n:
                continue
            cnts.append((temp['0'], temp['1']))

        dp = [[0] * (n + 1) for _ in range(m +  1)]
        cur_limit_0 = cur_limit_1 = 0
        for x in cnts:
            zero_num, one_num = x[0], x[1]
            cur_limit_0 = min(cur_limit_0 + zero_num, m)
            cur_limit_1 = min(cur_limit_1 + one_num, n)
            for j in range(cur_limit_0, zero_num - 1, -1):
                for k in range(cur_limit_1, one_num - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zero_num][k - one_num] + 1)
                    
        return dp[m][n] # 错误, 有小细节没处理好
    

class Solution:
    # 递推 + 空间优化 + 循环优化
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for str in strs:
            temp = Counter(str)
            if temp['0'] > m or temp['1'] > n:
                continue
            cnts.append((temp['0'], temp['1']))

        dp = [[0] * (n + 1) for _ in range(m +  1)]
        cur_limit_0 = cur_limit_1 = 0
        for x in cnts:
            zero_num, one_num = x[0], x[1]
            cur_limit_0 = min(cur_limit_0 + zero_num, m)
            cur_limit_1 = min(cur_limit_1 + one_num, n)
            for j in range(cur_limit_0, zero_num - 1, -1):
                for k in range(cur_limit_1, one_num - 1, -1):
                    temp = dp[j - zero_num][k - one_num] + 1
                    if temp > dp[j][k]:
                        dp[j][k] = temp # 手写max更快
                    
        return max(map(max, dp))    # 522ms
    

# 2025年12月27日
# No474
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for s in strs:
            cnt = Counter(s)
            if cnt["0"] > m or cnt["1"] > n:
                continue
            cnts.append((cnt["0"], cnt["1"]))

        length = len(cnts)
        @lru_cache(maxsize=None)
        def dfs(i: int, cnt0: int, cnt1:int):
            if i < 0:
                return 0
            # 不选
            res = dfs(i - 1, cnt0, cnt1)
            # 选
            cur_s0 = cnts[i][0]
            cur_s1 = cnts[i][1]
            if cur_s0 <= cnt0 and cur_s1 <= cnt1:
                res = max(res, dfs(i - 1, cnt0 - cur_s0, cnt1 - cur_s1) + 1)

            return res
        
        ans = dfs(length - 1, m, n)
        dfs.cache_clear()
        return ans

fmax = lambda x, y: x if x > y else y
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = []
        for s in strs:
            cnt = Counter(s)
            if cnt["0"] > m or cnt["1"] > n:
                continue
            cnts.append((cnt["0"], cnt["1"]))

        length = len(cnts)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
        for i, x in enumerate(cnts):
            num0, num1 = x[0], x[1]
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= num0 and k >= num1:
                        dp[i + 1][j][k] = fmax(dp[i][j][k], dp[i][j - num0][k - num1] + 1)
                    else:
                        dp[i + 1][j][k] = dp[i][j][k]

        return dp[-1][-1][-1]


fmax = lambda x, y: x if x > y else y
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count("0")
            cnt1 = len(s) - cnt0
            if cnt0 > m or cnt1 > n:
                continue
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= cnt0 and k >= cnt1:
                        dp[j][k] = fmax(dp[j][k], dp[j - cnt0][k - cnt1] + 1)

        return dp[-1][-1]


