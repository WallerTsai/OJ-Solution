from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [["."] * n for _ in range(m)]

        for i, row in enumerate(boxGrid):
            k = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    res[i][j] = "*"
                    k = j - 1
                elif row[j] == '#':
                    res[i][k] = "#"
                    k -= 1
        res = [list(row) for row in zip(*res[::-1])]
        return res
    
class Solution:
    # 灵神
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        ans = [['.'] * m for _ in range(n)]

        for i, row in enumerate(boxGrid):
            k = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':  # 障碍物
                    ans[j][-1 - i] = '*'
                    k = j - 1  # 障碍物左边最近的石头，在旋转后掉落到 j-1
                elif row[j] == '#':  # 石头
                    ans[k][-1 - i] = '#'  # 旋转后，石头掉落到 k
                    k -= 1

        return ans

