from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        ans = 0
        li = []
        for num in nums:
            if num < 0:
                num = -num
            l = bisect_left(li, (num  + 1) // 2)
            r = bisect_right(li, num * 2)
            ans += r - l
            li.append(num)
            li.sort()
        return ans
    
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        ans = 0
        li = SortedList()
        for num in nums:
            if num < 0:
                num = -num
            l = bisect_left(li, (num  + 1) // 2)
            r = bisect_right(li, num * 2)
            ans += r - l
            li.add(num)
        return ans



# 不妨设 ∣a∣<∣b∣,有
# min(∣a−b∣,∣a+b∣)=∣b∣−∣a∣
# max(∣a−b∣,∣a+b∣)=∣b∣+∣a∣
# 则
# min(∣a−b∣,∣a+b∣)=∣b∣−∣a∣<=min(∣a∣,∣b∣)=∣a∣
# 得到 ∣b∣<=2∗∣a∣
# max(∣a−b∣,∣a+b∣)=∣b∣+∣a∣>=max(∣a∣,∣b∣)=∣b∣
# 得到∣a∣>=0,此式恒成立

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        abs_nums = sorted(abs(num) for num in nums)
        n = len(abs_nums)
        ans = 0
        for i in range(n):
            b = abs_nums[i]
            low = (b + 1) // 2
            # high = 2 * b
            
            left = bisect_left(abs_nums, low, 0, i)
            # right = bisect_right(abs_nums, high, 0, i)
            # print(right == i)
            ans += i - left
            
        return ans
    
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        ans = left = 0
        for j, b in enumerate(nums):
            while abs(nums[left]) * 2 < abs(b):
                left += 1
            # a=nums[i]，其中 i 最小是 left，最大是 j-1，一共有 j-left 个
            ans += j - left
        return ans