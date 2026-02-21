from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if len(cardPoints) == k:
            return sum(cardPoints)
        
        cur_sum = sum(cardPoints[:k])
        res = cur_sum

        # left_p = k-1
        gab = len(cardPoints)-k
        for i in range(k-1,-1,-1):
            # right_p = gab + left_p
            right_p = gab + i
            cur_sum = cur_sum + cardPoints[right_p] - cardPoints[i]
            if cur_sum > res:
                res = cur_sum
        return res  # 9 - 12ms

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if len(cardPoints) == k:
            return sum(cardPoints)  
        
        cur_sum =  sum(cardPoints[-k:])
        res = cur_sum

        for left,right in zip(cardPoints[:k],cardPoints[-k:]):
            cur_sum = cur_sum + left - right
            if cur_sum > res:
                res = cur_sum

        return res  # 9 - 12ms


