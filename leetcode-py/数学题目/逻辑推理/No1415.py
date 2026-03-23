class Solution:
    # dfs 爆索
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << n - 1):
            return ""
        chars = ['a', 'b', 'c']
        res = []
        path = []
        def dfs(i: int):
            if i == n:
                res.append(''.join(path))
                return
            pre = path[i - 1] if i > 0 else None
            for cur in chars:
                if cur == pre:
                    continue
                path.append(cur)
                dfs(i + 1)
                path.pop()
            return
        
        dfs(0)
        return res[k - 1]
    


class Solution:
    # 数学
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 << (n - 1):
            return ''
        
        chars = ['a', 'b', 'c']
        res = []
        j, k = divmod(k - 1, 1 << n - 1)
        res.append(chars[j])

        for i in range(n - 1, 0, -1):
            j, k = divmod(k, 1 << i - 1)

            # https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/
            # No964 解法4
            if chars[j] >= res[-1]:
                choose = chars[j + 1]
            else:
                choose = chars[j]
                
            res.append(choose)
        
        return ''.join(res)
            