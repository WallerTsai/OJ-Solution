from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        MX = max(max(x for x in row) for row in grid)
        ans = 0
        for i in range(MX.bit_length() - 1, -1, -1):
            for row in grid:
                flag = False
                for x in row:
                    if x & 1 << i == 0:
                        flag = True
                        break
                if not flag:
                    ans |= 1 << i
        return ans  # 错误


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        MX = max(max(x for x in row) for row in grid)
        ans = 0
        for i in range(MX.bit_length() - 1, -1, -1):
            for row in grid:
                flag = False
                for x in row:
                    mask = (1 << i) - 1
                    t = ans | mask
                    if x & 1 << i == 0 and x | t == t:
                        flag = True
                        break
                if not flag:
                    ans |= 1 << i
        return ans
    
class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        def check(t, k, i):
            if (k >> i) & 1 != 0:
                return False
            low_mask = (1 <<(i + 1)) - 1
            high_mask = ~low_mask
            if ((k & high_mask) | t) != t:
                return False
            return True
        MX = max(max(x for x in row) for row in grid)
        ans = 0
        for i in range(MX.bit_length() - 1, -1, -1):
            for row in grid:
                flag = False
                for x in row:
                    if check(ans, x, i):
                        flag = True
                        break
                if not flag:
                    ans |= 1 << i
        return ans  # 888ms

class Solution:
    # 灵神
    def minimumOR(self, grid: List[List[int]]) -> int:
        mx = max(map(max, grid))
        ans = 0
        # 试填法：ans 的第 i 位能不能是 0？
        # 如果在每一行的能选的数字中，都存在第 i 位是 0 的数，那么 ans 的第 i 位可以是 0，否则必须是 1
        for i in range(mx.bit_length() - 1, -1, -1):
            mask = ans | ((1 << i) - 1)  # mask 低于 i 的比特位全是 1，表示 grid[i][j] 的低位是 0 还是 1 无所谓
            for row in grid:
                for x in row:
                    # x 的高于 i 的比特位，如果 ans 是 0，那么 x 的这一位必须也是 0
                    # x 的低于 i 的比特位，随意
                    # x 的第 i 个比特位，我们期望它是 0
                    if (x | mask) == mask:  # x 可以选，且第 i 位是 0
                        break
                else:  # 这一行的可选数字中，第 i 位全是 1
                    ans |= 1 << i  # ans 第 i 位必须是 1
                    break  # 填下一位
        return ans  # 67ms
Solution().minimumOR([[1,5],[2,4]])