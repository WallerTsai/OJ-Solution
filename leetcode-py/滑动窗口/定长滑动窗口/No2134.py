from math import inf
from typing import List
from collections import Counter

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        res = inf
        length = len(nums)
        count = Counter(nums)[1]

        if count == length or count == 0:
            return 0

        record = left = nums.index(0)  # 先找到第一个0的位置
        right = (left + 1 + length) % length

        while right != record:

            if nums[right] == 1:
                temp = 0
                i = right
                for _ in range(count):
                    if nums[i] == 0:
                        temp += 1
                    i = (i+1+length) % length
                if temp < res:
                    res = temp
            right = (right + 1 + length) % length

        return res  # 超时

        
class Solution:
# 作者：yusir
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        s = sum(nums[0:k])
        res = k - s
        for i in range(1,n):
            s += nums[(i+k-1)%n] - nums[i-1]
            res = min(res, k - s)
        return res  # 134ms


class Solution:
    # 参考了leetcode最快解法
    def minSwaps(self, nums: List[int]) -> int:
        sum_nums = sum(nums)

        if sum_nums == len(nums) or sum_nums == 0:
            return 0
        
        new_nums = nums + nums # 两个相同字符串拼接,省去队列结构

        temp = 0
        new_sum = sum(new_nums[:sum_nums])
        if new_sum == sum_nums:
            return 0
        for i in range(len(nums)-1):
            new_sum = new_sum - new_nums[i] + new_nums[sum_nums+i]
            if new_sum > temp:
                temp = new_sum
        return sum_nums - temp  # 35ms



# 2026年1月26日
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total == n:
            return 0

        nums = nums + nums
        rec = cur = sum(nums[:total])
        for i in range(n - 1):
            cur -= nums[i]
            cur += nums[i + total]
            rec = max(rec, cur)
        return total - rec  # 44ms
