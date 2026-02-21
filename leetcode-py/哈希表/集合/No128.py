from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = 0
        for num in nums:
            count = 0
            while num in nums:
                count += 1
                num += 1
            n = max(n, count)
        return n   # O(n ** 2)
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = 0
        for num in nums:
            if num - 1 in nums:
                continue

            nx = num + 1
            while nx in nums:
                nx += 1

            n = max(n, nx - num)

        return n    # 43ms
    

class Solution:
    # 灵神
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)  # 把 nums 转成哈希集合
        m = len(st)

        ans = 0
        for x in st:  # 遍历哈希集合
            if x - 1 in st:  # 如果 x 不是序列的起点，直接跳过
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
            if ans * 2 >= m:  # ans 不可能变得更大
                break
        return ans

