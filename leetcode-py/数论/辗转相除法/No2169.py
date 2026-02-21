class Solution:
    # 辗转相除法
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num2 > 0:
            ans += num1 // num2
            num1, num2 = num2, num1 % num2
        return ans



