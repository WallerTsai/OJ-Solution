from typing import List


class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 4:
            return []

        flat = False
        ans = []
        path = [[0, 1]]
        m = n * (n - 1)
        
        def dfs(a, used: set, pre: list):
            nonlocal flat
            if a == m:
                nonlocal ans
                ans = path[:]
                flat = True
            
            pre_1, pre_2 = pre
            for i in range(0, n):
                if i == pre_1 or i == pre_2:
                    continue
                for j in range(0, n):
                    if j == i or j == pre_1 or j == pre_2:
                        continue
                    if (i, j) not in used:
                        used.add((i, j))
                        path.append([i, j])
                        dfs(a + 1, used, [i, j])
                        path.pop()
                        used.remove((i, j))
                        if flat:
                            return
            return
        
        used = {(0, 1)}
        dfs(1, used, [0, 1])
        return ans  # 超时
    

class Solution:
    # 灵神
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n < 5:
            return []

        ans = []

        # 单独处理 d=1
        for i in range(0, n, 2):
            ans.append([i, (i + 1) % n])
        for i in range(1, n, 2):
            ans.append([i, (i + 1) % n])
        if n % 2 == 0:  # 保证 d=1 的最后一场比赛与 d=2 的第一场比赛无冲突
            ans[-1], ans[-2] = ans[-2], ans[-1]

        # 处理 d=2,3,...,n-2
        for d in range(2, n - 1):
            for i in range(n):
                ans.append([i, (i + d) % n])

        # 单独处理 d=n-1（或者说 d=-1）
        for i in range(1, n, 2):
            ans.append([i, (i - 1) % n])
        if n % 2 == 0:  # 保证 i 为奇数时的最后一场比赛与 i 为偶数时的第一场比赛无冲突
            ans[-1], ans[-2] = ans[-2], ans[-1]
        for i in range(0, n, 2):
            ans.append([i, (i - 1) % n])

        return ans
    
fun = Solution()
fun.generateSchedule(5)


# 难