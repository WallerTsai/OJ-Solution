from itertools import pairwise


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = list(map(int,s))
        while len(nums) != 2:
            temp = []
            for a,b in pairwise(nums):
                temp.append((a+b) % 10)
            nums = temp
        return nums[0] == nums[-1]

fun = Solution()
print(fun.hasSameDigits(s="3902"))