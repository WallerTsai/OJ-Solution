
# (a + b) ^ 2 >= a ^ 2 + b ^ 2
# 直接贪心即可, 剩余位置补0
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        path = []
        for _ in range(num):
            if sum > 9:
                path.append(9)
                sum -= 9
            elif sum > 0:
                path.append(sum)
                sum -= sum
            else:
                path.append(0) 
        return ''.join(map(str, path)) if not sum else ""
