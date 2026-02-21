from collections import Counter, deque
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left =  0
        dq = deque()
        nums.sort()
        ans = 0
        for right in range(1,len(nums)):
            if nums[right] != nums[right - 1]:
                dq.append(right)
            if nums[right] - nums[left] == 1:
                ans = max(right - left + 1, ans)
            elif nums[right] - nums[left] > 1:
                left = dq.popleft() if dq else 0

        return ans  # 51ms

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        return max(v + cnts[k+1] if k + 1 in cnts else 0 for k,v in cnts.items())

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        ans = i = j = 0
        while i < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            nxt = j
            while j < len(nums) and nums[j] == nums[i] + 1:
                j += 1
            if j > nxt:
                ans = max(ans, j - i)
            i = nxt
        return ans

fun = Solution()
fun.findLHS([1,2,-1,1,2,5,2,5,2])

