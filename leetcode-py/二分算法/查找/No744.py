from typing import List
from bisect import bisect_left,bisect_right

class Solution:
    # 暴力
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]   # 0ms
    
class Solution:
    # 二分库
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect_right(letters,target)
        return letters[index] if index != len(letters) else letters[0]
        # 0ms

class Solution:
# 作者：Benhao
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return min(letters, key=lambda x:(ord(x) - ord(target) - 1)%26)

class Solution:
# 作者：Benhao
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[r] if (r := bisect_right(letters, target)) < len(letters) else letters[0]

class Solution:
    # 手写二分
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 闭区间
        left,right = 0,len(letters)-1
        while left <= right:
            mid = (left+right)//2

            # if letters[mid] < target:
            #     left = mid + 1
            # else:
            #     right = mid -1

            # 不能相等
            if letters[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        return letters[left] if left != len(letters) else letters[0] # 0ms


