import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        length1 = len(str1)
        length2 = len(str2)

        m = math.gcd(length1,length2)

        for i in range(m,0,-1):
            if length1 % i != 0 or length2 % i != 0:
                continue
            temp = str1[:i]
            if temp * (length1 // i) == str1 and temp * (length2 // i) == str2:
                return str1[:i]
        return ""


class Solution:
    # 辗转处理
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while True:
            if   str1 == str2         : return str1
            elif str1.startswith(str2): str1 = str1[len(str2) :]
            elif str2.startswith(str1): str2 = str2[len(str1) :]
            else                      : return ""
