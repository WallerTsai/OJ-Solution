from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            x_ = x + i
            y_ = y
            for j in range(k):
                grid[x_][y_], grid[2 * x + k - 1 - x_][y_] = grid[2 * x + k - 1 - x_][y_], grid[x_][y_]
                y_ += 1
            x_ += 1

        return grid
    
class Solution:
    # 双指针
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l, r = x, x + k - 1
        while l < r:
            for j in range(y, y + k):
                grid[l][j], grid[r][j] = grid[r][j], grid[l][j]
            l += 1
            r -= 1
        return grid

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        lis = []
        for row in grid[x: x+k]:
            lis.append(row[y: y+k])
        lis = lis[::-1]
        for i in range(x, x+k):
            grid[i][y: y+k] = lis[i-x]
        return grid


        

fun = Solution()
fun.reverseSubmatrix([[3,4,2,3],[2,3,4,2]], 0, 2, 2)