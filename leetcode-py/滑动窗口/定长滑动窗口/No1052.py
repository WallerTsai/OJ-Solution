from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        length = len(customers)
        res = sum(customers[i] for i in range(minutes) if grumpy[i] == 0)

        cur_sum = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_part = cur_sum

        for i in range(minutes,length):
            if grumpy[i-minutes] == 1:
                cur_sum -= customers[i-minutes]
            if grumpy[i] == 0:
                res += customers[i]
            else:
                cur_sum += customers[i]
                max_part = max(max_part,cur_sum)
        
        return res+max_part #11ms

fun = Solution()
outcome = fun.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3)
print(outcome)