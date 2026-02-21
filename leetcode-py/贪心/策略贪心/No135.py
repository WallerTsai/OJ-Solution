from typing import List


class Solution:
    # 两次遍历
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                l[i] = l[i - 1] + 1
        for i in range(n  - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                l[i] = max(l[i + 1] + 1, l[i])
        print(l)
        return sum(l)   # 15ms
    

class Solution:
    # leetcode 
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)
        
        return ret
    
class Solution:
    # leetcode 一次遍历
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1
        
        return ret
    
f = Solution()
f.candy([1,3,4,5,2])