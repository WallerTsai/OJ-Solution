from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        ans = 0
        for i in machines:
            ans = max(ans, abs(avg - i))
        return ans # 错误
    
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        ans = temp = 0  # temp 为负则需要向左边传， 为正则为上轮向右传
        for i in machines:
            if temp < 0 and temp + i > avg:
                # 两边都送
                ans = max(ans, i - avg)
                temp += i -avg
            else:
                temp += i -avg
                ans = max(ans, abs(temp))   # 可以证明前面 欠或多 多少就需要多少次解决

        return ans
    
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        ans = temp = 0  # temp 为负则需要向左边传， 为正则为上轮向右传
        for i in machines:
            if temp < 0 and temp + i > avg:
                # 两边都送
                ans = max(ans, i - avg)
            else:
                ans = max(ans, abs(temp))   # 可以证明前面 欠或多 多少就需要多少次解决

            temp += i - avg
            
        return ans