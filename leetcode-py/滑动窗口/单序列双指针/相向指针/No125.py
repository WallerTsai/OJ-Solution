# 库函数大战

import re


class Solution:
    # 库函数
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]
# 在 Python 中，当你将一个函数作为参数传递给另一个函数时，通常不需要在该函数名后面加上括号。
# 这是因为加上括号表示立即调用该函数，而没有括号则表示传递函数对象本身。

# str.isalnum 是一个函数对象，表示 str 类型的 isalnum 方法。
# filter 函数需要两个参数：一个函数对象和一个可迭代对象。
# 传递 str.isalnum 作为第一个参数，表示 filter 会将 s.lower() 中的每个元素传递给 str.isalnum 方法，并根据其返回值（True 或 False）来决定是否保留该元素。

class Solution:
    # 正则库函数
    def isPalindrome(self, s: str) -> bool:
            tmp = re.sub(r"[^A-Za-z0-9]","", s).lower()
            return tmp == tmp[::-1]
    
class Solution:
    # 库函数 + 双指针
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 排查非字母字符
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

class Solution:
    # 手写库函数(利用ASCII表) + 双指针
    
    def is_letters_digits(self,c):
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9'
    
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 排查非字母字符
            while left < right and not self.is_letters_digits(s[left]):
                left += 1
            while left < right and not self.is_letters_digits(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True # 慢

# str.isalnum() 是一个内置方法，它在底层是用 C 语言实现的，经过了高度优化。
# Python 的内置方法通常比纯 Python 实现的方法更快，因为它们直接调用底层的 C 代码，
# 减少了 Python 解释器的开销

