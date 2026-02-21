from collections import defaultdict
from functools import cache, reduce
from typing import Iterator, List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        MX = [0] * n
        
        temp = 0
        for i in range(n - 1, -1, -1):
            temp |= nums[i]
            MX[i] = temp

        def check(the_set: set) -> int:
            res = 0
            for num in the_set:
                res |= num
            return res

        ans = list(range(n,0,-1))
        left = 0
        a_set = set()
        for right, num in enumerate(nums):
            a_set.add(num)
            while left <= right and check(a_set) == MX[left]:
                ans[left] = right - left + 1
                if nums[left] in a_set:
                    a_set.remove(nums[left])
                left += 1

        return ans  #错误

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        MX = [0] * n
        
        temp = 0
        for i in range(n - 1, -1, -1):
            temp |= nums[i]
            MX[i] = temp

        cnt = defaultdict(int)
        def check() -> int:
            res = 0
            for num in cnt:
                res |= num
            return res

        ans = list(range(n,0,-1))
        left = 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            while left <= right and check() == MX[left]:
                ans[left] = right - left + 1
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1

        return ans  # 235ms

class Solution:
    # 灵神
    # 滑动窗口 + 栈
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[-1] = 1
        if n == 1:
            return ans

        # 保证栈中至少有两个数，方便判断窗口右端点是否要缩小
        nums[-1] |= nums[-2]
        left_or, right, bottom = 0, n - 1, n - 2
        for left in range(n - 2, -1, -1):
            left_or |= nums[left]
            # 子数组 [left,right] 的或值 = 子数组 [left,right-1] 的或值，说明窗口右端点可以缩小
            while right > left and (left_or | nums[right]) == (left_or | nums[right - 1]):
                right -= 1
                # 栈中只剩一个数
                if bottom >= right:
                    # 重新构建一个栈，栈底为 left，栈顶为 right
                    for i in range(left + 1, right + 1):
                        nums[i] |= nums[i - 1]
                    bottom = left
                    left_or = 0
            ans[left] = right - left + 1
        return ans

fun = Solution()
fun.smallestSubarrays([76,57,77,64,41,82,34,57,94,33,87,24,17,54,11,10,18,70,80,37,18,5,11,71,0,29,90,45,25,64,64,32,3,67,78,4,98,2,50,100,9,97,48,47,23,28,25,45,56,37,30,72,57,58,39,89,78,13,76,40,44,79,41,99,24,7,86,23,42,58,34,14,11,26])