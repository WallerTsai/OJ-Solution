from string import ascii_lowercase
from typing import List


class Solution:
    # 暴力模拟
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        words = [0]
        for op in operations:
            if len(words) >= k:
                break
            if op:
                words += [(i + 1) % 26 for i in words]
            else:
                words += words
        return chr(words[k - 1] + ord('a')) # 超时



class Solution:
# 作者：wxyz
# 链接：https://leetcode.cn/problems/find-the-k-th-character-in-string-game-ii/solutions/3714694/si-jie-mo-ni-er-jin-zhi-hui-su-shu-xue-j-ya06/
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # 构建 shift 掩码：每一位代表是否是 shift 操作
        mask = 0
        for i, op in enumerate(operations):
            if op == 1:  # 这一层是 shift，把第 i 位设置为 1
                mask |= (1 << i)

        # 检查每一位是否落在 shift 部分
        positions = (k - 1) & mask
        # 统计总 shift 的次数
        count = positions.bit_count()

        # 'a' 向后偏移 count 个字母
        return chr(count % 26 + ord('a'))


class Solution:
    # 递归
    # cv by 灵神
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if not operations:
            return 'a'
        op = operations.pop()
        m = 1 << len(operations)

        if k <= m:  # k 在左半段
            return self.kthCharacter(k, operations)
        
        # 右半段
        ans = self.kthCharacter(k - m, operations)
        return chr((ord(ans) - ord('a') + op) % 26 + ord('a'))


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        m = (k - 1).bit_length()
        inc = 0
        for i in range(m - 1, -1, -1):
            if k > 1 << i:  # k 在右半段
                inc += operations[i]
                k -= 1 << i
        return ascii_lowercase[inc % 26]
    

# 2026年3月3日
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        rev = 0
        while operations:
            op = operations.pop()
            if k > 1 << len(operations):
                rev += op
                k -= 1 << len(operations)
        return ascii_lowercase[rev % 26]
