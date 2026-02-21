from random import randrange
from typing import List


class Solution:
    # 暴力
    def repeatedNTimes(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)


# 用一个临时变量储存nums中的一个数，使得剩下的数数量为 2n - 1
# 如果 nums[0] 在下标 [1,n−1] 中出现过，那么返回 nums[0]。
# 否则，去掉 nums[0]，剩下 2n−1 个数，出现次数为 n 的那个数变成绝对众数，可以用 169 题的算法解决。
class Solution:
    # 灵神
    # 摩尔投票
    def repeatedNTimes(self, nums: List[int]) -> int:
        ans = hp = 0
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == temp:
                return temp
            if hp == 0:  # x 是初始擂主，生命值为 1
                ans, hp = nums[i], 1
            else:  # 比武，同门加血，否则扣血
                hp += 1 if nums[i] == ans else -1
        return ans

# 在 nums 中随机选择两个下标不同的元素，如果两数相等，即找到了重复元素。

# 首先，在 [0,n−1] 中随机一个数，作为下标 i。
# 然后，我们要在 [0,i−1]∪[i+1,n−1] 中随机另一个下标 j。
# 但是，标准库只支持在一个连续范围中随机元素，如何在一个间断的区间中随机元素呢？
# 考虑映射，把 [0,n−2] 映射到 [0,i−1]∪[i+1,n−1] 中：
# f(x)={ 
# x, 0≤x≤i−1
# x+1, i≤x≤n−2

# 具体地，在 [0,n−2] 中随机一个数 x：
# 如果 x<i，那么把 x 作为下标 j。
# 如果 x≥i，那么把 x+1 作为下标 j。

class Solution:
    # 灵神
    # 随机化
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            # 在 [0, n-1] 中随机生成两个不同下标
            i = randrange(n)
            j = randrange(n - 1)
            if j >= i:
                j += 1
            if nums[i] == nums[j]:
                return nums[i]