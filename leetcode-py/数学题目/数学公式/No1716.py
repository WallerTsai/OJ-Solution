class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        t = 0
        for i in range(n):
            if i and i % 7 == 0:
                t += 1
            ans += i % 7 + 1 + t
        return ans
    

class Solution:
    # 数学公式
    def totalMoney(self, n):
        total = 0
        week, day = divmod(n, 7)
        # total += 28 * week + (week - 1) * week * 7 // 2 
        total += week * (week + 7) * 7 // 2 # 合并后
        total += (week + 1  + week + day ) * day // 2
        return total