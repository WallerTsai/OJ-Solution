from math import inf
from typing import List


# class Solution:
#     def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#         index = []
#         for i, num in enumerate(nums):
#             if num == key:
#                 index.append(i)

#         ans = set()
#         n = len(nums)
#         for i in index:
#             for j in range(max(i - k, 0), min(i + k, n - 1) + 1):
#                 ans.add(j)
        
#         return sorted(list(ans))    # 176ms
    
# class Solution:
#     def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#         n = len(nums)
#         ans = set()
#         for i, num in enumerate(nums):
#             if num == key:
#                 for j in range(max(i - k, 0), min(i + k, n - 1) + 1):
#                     ans.add(j)
        
#         return sorted(list(ans))    # 179ms
    

class Solution:
    # 灵神
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        last = -inf
        for i in range(k - 1, -1, -1):
            if nums[i] == key:
                last = i
                break

        ans = []
        n = len(nums)
        for i in range(n):
            if i + k < n and nums[i + k] == key:
                last = i + k
            if last >= i - k:  # key 在窗口中
                ans.append(i)
        return ans
    
fun = Solution()
ans = fun.findKDistantIndices([3,4,2,1,3,9,5], 9, 1)
print(ans)