from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        i = 1
        ans = []
        while i != 0:
            if i <= n:
                ans.append(i)
                i *= 10
            else:
                i //= 10
                i += 1
                if i % 10 == 9:
                    break
        return ans  # 想不出来

# 没想到这个递归居然是O(n)的
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(i: int):
            if i <= n:
                yield i
                i *= 10
                if i <= n:
                    for j in range(10):
                        yield from dfs(i + j)
        
        ans = []
        for i in range(1, 10):
            ans.extend(dfs(i))
        
        return ans


fun = Solution()
fun.lexicalOrder(2)


