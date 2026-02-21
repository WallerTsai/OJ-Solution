from itertools import accumulate, pairwise
from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)

        # 前缀和
        pre = skill[:]
        for i in range(1,n):
            pre[i] += pre[i-1]

        # 用一个数组记录一下该轮每人的结束时间
        finish_time = [0] * n

        for k in mana:
            # 找到极限时间
            start_time = finish_time[0]
            for i in range(n-1):
                need = finish_time[i+1] - pre[i] * k
                start_time = max(start_time, need)
            # 更新数值
            temp = start_time
            for i,sk in enumerate(skill):
                temp += sk * k
                finish_time[i] = temp
        
        return finish_time[-1]

fun = Solution()
fun.minTime([1,3,4],[2,3,3,3])


# 灵神题解
# https://leetcode.cn/problems/find-the-minimum-amount-of-time-to-brew-potions/solutions/3624232/zheng-fan-liang-ci-sao-miao-pythonjavacg-5fz9/

class Solution:
    # 模拟
    # 正反两次扫描
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        last_finish = [0] * n  # 第 i 名巫师完成上一瓶药水的时间
        for m in mana:
            # 按题意模拟
            sum_t = 0
            for x, last in zip(skill, last_finish):
                if last > sum_t: sum_t = last  # 手写 max
                sum_t += x * m
            # 倒推：如果酿造药水的过程中没有停顿，那么 last_finish[i] 应该是多少
            last_finish[-1] = sum_t
            for i in range(n - 2, -1, -1):
                last_finish[i] = last_finish[i + 1] - skill[i + 1] * m
        return last_finish[-1]  # 9609ms


class Solution:
    # 公式推导
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        s = list(accumulate(skill, initial=0))  # skill 的前缀和
        start = 0
        for pre, cur in pairwise(mana):
            start += max(pre * s[i + 1] - cur * s[i] for i in range(n))
        return start + mana[-1] * s[-1] # 5563ms
    

class Solution:
    # record
    # 数学分析，非常妙
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        s = list(accumulate(skill, initial=0))

        suf_record = [n - 1]
        for i in range(n - 2, -1, -1):
            if skill[i] > skill[suf_record[-1]]:
                suf_record.append(i)

        pre_record = [0]
        for i in range(1, n):
            if skill[i] > skill[pre_record[-1]]:
                pre_record.append(i)

        start = 0
        for pre, cur in pairwise(mana):
            record = pre_record if pre < cur else suf_record
            start += max(pre * s[i + 1] - cur * s[i] for i in record)
        return start + mana[-1] * s[-1]
