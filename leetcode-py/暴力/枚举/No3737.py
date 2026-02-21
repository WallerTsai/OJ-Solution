from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        li = [0]
        for x in nums:
            li.append(li[-1] + (x == target))

        print(li)

        ans = 0
        for i in range(1, n + 1):
            for j in range(i):
                length = i - j
                if li[i] - li[j] > length // 2:
                    ans += 1

        return ans

fun = Solution()
fun.countMajoritySubarrays([1,2,2,3], 2)
