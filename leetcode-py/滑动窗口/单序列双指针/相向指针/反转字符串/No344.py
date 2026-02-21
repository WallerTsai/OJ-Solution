from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        temp = ''

        while left<right:

            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1

        while left<right:

            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s[:] = s[::-1] 是切片赋值语法，表示用 s[::-1] 替换 s 中的元素。
        # 注意不能写成 s = s[::-1]，因为 s 只是形参，修改 s 不会影响函数外部传入的实参。
        # 注意这不是原地操作，需要 O(n) 额外空间。
        s[:] = s[::-1]