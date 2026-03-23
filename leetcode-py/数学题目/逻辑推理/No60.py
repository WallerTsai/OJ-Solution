import math


class Solution:
    # dfs 爆索
    def getPermutation(self, n: int, k: int) -> str:
        if k > math.factorial(n):
            return ""
        chars = []
        for i in range(1, n + 1):
            chars.append(str(i))
        res = []
        path = []
        visited = set()
        def dfs(i: int):
            if i == n:
                res.append(''.join(path))
                return
            for cur in chars:
                if cur in visited:
                    continue
                path.append(cur)
                visited.add(cur)

                dfs(i + 1)

                path.pop()
                visited.remove(cur)
            return
        
        dfs(0)
        return res[k - 1]   # 超时
    

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        chars = [str(i) for i in range(1, n + 1)]
        res = []
        t = math.factorial(n)
        for i in range(n , 0, -1):
            t //= i
            j = (k - 1) // t # ceil(k / t) - 1
            res.append(chars[j])
            chars.pop(j)
            k %= t
        return ''.join(res)

