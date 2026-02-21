from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort(reverse=True)
        pre = nums[0]
        for n in nums:
            if n == pre:
                if pre >= k:
                    continue
                else:
                    return -1
            elif n > k:
                ans += 1
                pre = n
            elif n < k:
                return -1
        return ans + 1 if pre != k else ans

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        if k > mn:
            return -1
        return len(set(nums)) - (k == mn)

fun = Solution()
fun.minOperations([9,7,5,3],1)


