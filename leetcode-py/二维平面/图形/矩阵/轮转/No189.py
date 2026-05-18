from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        left, right = n - k - 1, n - 1
        while left >= 0:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left -= 1

        left = n % k
        if left:
            while right != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                if left > 0:
                    left -= 1   # 错误



class Solution:
    # 灵神
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等于轮转 k % n 次
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

