from collections import defaultdict
from functools import cache

MOD = 1_000_000_007
class Solution:
    def numOfWays(self, n: int) -> int:
        li = []
        path = []
        def dfs(i: int, pre: int):
            if i == 3:
                li.append(path.copy())
                return
            for j in range(3):
                if j == pre:
                    continue
                path.append(j)
                dfs(i + 1, pre = j)
                path.pop()

        dfs(0, -1)

        amap = defaultdict(list)
        for i in range(len(li)):
            for j in range(i):
                flag = True
                for k in range(3):
                    if li[i][k] == li[j][k]:
                        flag = False
                        break
                if flag:
                    amap[i].append(j)
                    amap[j].append(i)

        @cache
        def trackback(i: int, pre: int):
            if i == n - 1:
                return 1
            res = 0
            for nx in amap[pre]:
                res = (res + trackback(i + 1, nx)) % MOD
            return res
        
        ans = 0
        for cur in amap:
            ans = (ans + trackback(0, cur)) % MOD

        return ans