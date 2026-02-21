from math import inf


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        sum_Y = sum(ch == "Y" for ch in customers)
        count_N = 0
        total = sum_Y
        t = 0
        for i, cus in enumerate(customers, start=1):
            if cus == "Y":
                sum_Y -= 1
            else:
                count_N += 1
            if sum_Y + count_N < total:
                total = sum_Y + count_N
                t = i
        return t

# 思想 打个比方，绝对温度下冰点为 273K，摄氏温度下冰点为 0 摄氏度。如果只关心哪一天最冷，用哪个单位计算都可以。
# 也就是把初始值 sum_Y -> 0
class Solution:
    # 灵神一次遍历
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = penalty = ans = 0
        for i, c in enumerate(customers):
            penalty += 1 if c == 'N' else -1
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i + 1
        return ans