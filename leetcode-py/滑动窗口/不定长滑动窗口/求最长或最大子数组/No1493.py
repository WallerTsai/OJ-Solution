from math import inf
from typing import List
class Solution:
    # 不定长滑动窗口+双指针+一定位指针
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zero_index = -1
        left = 0
        for right,num in enumerate(nums):
            if num == 0:
                res = max(res,right-left-1)
                if zero_index != -1:
                    left = zero_index+1
                zero_index = right
        if zero_index != -1:
            res = max(res,len(nums)-left-1)
        else:
            res = len(nums) - 1
        return res  # 40ms

class Solution:
    # 统计特定的下标 + 边界处理
    # 这里有效解决了边界的情况
    def longestSubarray(self, nums: List[int]) -> int:
        zero_index = [-1]   # 左边界
        # 统计0的下标
        zero_index += [i for i,num in enumerate(nums) if num == 0]
        zero_index += [len(nums)]   # 右边界

        # 数组中 0 的个数不超过1个
        if len(zero_index) <= 3:
            return len(nums) - 1

        res = 0
        for i in range(2,len(zero_index)):
            res = max(res,zero_index[i]-zero_index[i-2]-2)
        return res
    
class Solution:
    # leetcode 最快
    # 难读 ：大概就是统计步长
    def longestSubarray(self, nums: List[int]) -> int:
        num_0 = 0
        LEFT = RIGHT = 0
        max_len = 0
        for one in nums:
            if one == 0:
                if num_0 > 0:
                    LEFT = RIGHT = 0
                else:
                    max_len = max(max_len, LEFT + RIGHT)
                    # 遇到单个0，则移动右边到左边，清空右边
                    LEFT = RIGHT
                    RIGHT = 0
                num_0 += 1
            else:
                # 永远只填充右边的变量
                RIGHT += 1
                num_0 = 0
        if RIGHT:
            max_len = max(max_len, LEFT + RIGHT)
        return min(max_len, len(nums) - 1)
    
class Solution:
    # 记区间 0 的个数 + 双指针
    def longestsubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        left, right = 0, 0
        cnt_zeros = 0 

        while right < n:
            if nums[right] == 0:
                cnt_zeros += 1
            while cnt_zeros > 1:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            res = max(res, right - left)
            right += 1
        return res  # 75ms
    
class Solution:
    # 维护两个区间1的个数 p1:包含一个0的区间 p2:不包含0的区间
    # 动态规划(参考他人) -> 递推
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        p1 = p2 = 0
        for num in nums:
            if num == 0:
                p1 , p2 = p2 , 0
            else:
                p1 += 1
                p2 += 1
            res = max(res,p1)
        
        if res == len(nums):    # 全1情况,特殊处理
            res -= 1
        
        return res  # 54ms
    
class Solution:
    # 只增大的伪定长滑动窗口
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1
        for right,num in enumerate(nums):
            if num == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
        return right - left # 27ms



