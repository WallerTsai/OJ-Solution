from typing import List
from sortedcontainers import SortedList # type: ignore

class Solution:
    # 有序集合
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        sum_left = sum(nums[:dist + 2])
        left_list = SortedList(nums[1:dist + 2])
        right_list = SortedList()

        def left_to_right():
            x = left_list.pop()
            nonlocal sum_left
            sum_left -= x
            right_list.add(x)

        def right_to_left():
            x = right_list.pop(0)
            nonlocal sum_left
            sum_left += x
            left_list.add(x)

        while len(left_list) > k:
            left_to_right()

        ans = sum_left
        n = len(nums)
        for i in range(dist + 2, n):
            out_x = nums[i - dist -1]
            if out_x in left_list:
                sum_left -= out_x
                left_list.remove(out_x)
            else:
                right_list.remove(out_x)

            in_x = nums[i]
            if in_x < left_list[-1]:
                sum_left += in_x
                left_list.add(in_x)
            else:
                right_list.add(in_x)

            if len(left_list) == k - 1:
                right_to_left()
            elif len(left_list) == k + 1:
                left_to_right()

            ans = min(ans, sum_left)

        return ans




