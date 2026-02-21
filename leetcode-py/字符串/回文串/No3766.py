from bisect import bisect_left
from typing import List


is_Palindrome = []
for i in range(0, 10000 + 1):
    b = bin(i)[2:]
    if b == b[::-1]:
        is_Palindrome.append(i)
        
class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            i = bisect_left(is_Palindrome, num)
            pre = is_Palindrome[i - 1]
            suf = is_Palindrome[i]
            ans.append(min(num - pre, suf - num))
        return ans
