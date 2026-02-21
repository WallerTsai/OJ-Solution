from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    # 外层记录该层字符串，内层枚举下一层的bottom
    # cache + 中途退出
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        amap = defaultdict(set)
        for s in allowed:
            amap[s[:2]].add(s[2])

        ans = False

        @cache
        def dfs(s: str):
            nonlocal ans
            if ans or len(s) == 1:
                ans = True
                return 
            path = []
            n = len(s)

            def dfs2(i: int):
                if i == n - 1:
                    dfs("".join(path))
                    return
                for ch in amap[s[i: i + 2]]:
                    path.append(ch)
                    if dfs2(i + 1):
                        return
                    path.pop()
                return

            dfs2(0)
            return 

        ans = False
        dfs(bottom)
        return ans  # 255ms



from typing import List
from itertools import product
from collections import defaultdict
from functools import lru_cache

class Solution:
    # 草莓奶昔
    # 笛卡尔积
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        cand = defaultdict(lambda: defaultdict(set))
        for left, right, up in allowed:
            cand[left][right].add(up)

        @lru_cache(None)
        def dfs(char: str) -> bool:
            if len(char) <= 1:
                return True
            # 可取组合的笛卡尔积
            for nextLevel in product(*(cand[left][right] for left, right in zip(char, char[1:]))):
                if dfs(nextLevel):
                    return True
            return False

        return dfs(bottom)  # 99ms



class Solution:
    # 灵神
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        amap = defaultdict(set)
        for s in allowed:
            amap[s[:2]].add(s[2])

        n = len(bottom)
        f = [[] for _ in range(n)]
        f[-1] = bottom

        visited = set()
        def dfs(i: int, j: int):
            if i < 0:
                return True
            
            row = ''.join(f[i])
            if row in visited:
                return False
            
            if j == i + 1:  # 下一行
                visited.add(row)
                return dfs(i - 1, 0)
            
            for ch in amap[f[i + 1][j]  + f[i + 1][j + 1]]:
                f[i].append(ch)
                if dfs(i, j + 1):   # 这一行的下一个
                    return True
                f[i].pop()
                
            return False
        
        return dfs(n - 2, 0)    # 31ms