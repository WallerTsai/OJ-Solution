from bisect import bisect_left, bisect_right
from collections import deque
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = bisect_left(nums[i+1:],lower-nums[i])
            right = bisect_right(nums[i+1:],upper-nums[i])
            res += right-left
        return res  # 超时

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        dq = deque(nums[:])
        res = 0
        for i in range(len(nums)):
            if nums[i] * 2 > upper:
                break
            dq.popleft()
            left = bisect_left(dq,lower-nums[i])
            right = bisect_right(dq,upper-nums[i])
            res += right-left
        return res  # 1392ms

class Solution:
    # 灵神
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, 0, j)  # <= upper-nums[j] 的 nums[i] 的个数
            l = bisect_left(nums, lower - x, 0, j)  # < lower-nums[j] 的 nums[i] 的个数
            ans += r - l
        return ans

class Solution:
    # leetcode 大佬
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result   # 121ms

"""
以下是自己的解读：
countFairPairs 方法：
首先对数组 nums 进行排序。
调用 lower_bound 方法，分别计算和小于 upper + 1 和和小于 lower 的对的数量。
通过相减，得到满足 lower ≤ nums[i] + nums[j] ≤ upper 的对的数量。
有点类似概率论的 P(a<X<=b) = F(b) - F(a)


lower_bound 方法：
使用双指针法计算数组中和小于 value 的对的数量。
left 指针从数组的起始位置开始，right 指针从数组的末尾开始。
如果 nums[left] + nums[right] < value，说明所有 (left, right) 之间的对都满足条件，因此将 right - left 加到结果中，并将 left 向右移动一位。
如果 nums[left] + nums[right] ≥ value，说明当前对不满足条件，将 right 向左移动一位。

为什么 res += right - left ? 
(left, right) 之间的对 这里的对指的是
(nums[left],nums[left+1]) , (nums[left],nums[left+2]) ... (nums[left],nums[right])
举个例子：
[0,1,7,4,4,5].sort() -> [0,1,4,4,5,7]
执行lower_bound(nums, 7)
right左移到下标4这
此时nums[left] + nums[right] = 0 + 5 < 7
所以就有(0,1) (0,4) (0,4) (0,5) 一共 right-left=4个数对满足条件
left右移...
(1,4) (1,4) (1,5) 3个 ...
执行lower_bound(nums, 3)
(0,1) 1个

于是结果为 (4+3) - (1) = 6



"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        dq = deque(nums)
        res = 0
        while dq:
            num = dq.popleft()
            if num * 2 > upper:
                break
            left = bisect_left(dq,lower-num)
            right = bisect_right(dq,upper-num)
            res += right-left
        return res  # 1346ms
    
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        out_nums = SortedList()
        res = 0
        for num in nums:
            left = bisect_left(out_nums,lower-num)
            right = bisect_right(out_nums,upper-num)
            res += right-left
            out_nums.add(num)
        return res  # 8638ms