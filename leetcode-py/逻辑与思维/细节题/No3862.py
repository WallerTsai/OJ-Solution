class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        left = sum(nums)
        right = 1
        for i in range(n - 1, 0, -1):
            x = nums[i]
            left -= x
            # 提前中转
            if left < right:
                break
            # 提前返回
            if left == right:
                return i
            right *= x
        return -1