# 难度中等
from typing import List
# class Solution:
#     def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
#         the_list = [x for x in range(1,n+1) if x not in banned]
#         for i,value in enumerate(the_list):
#             if value <= maxSum:
#                 maxSum -= value
#             else:
#                 return i

#         return len(the_list)    # 超时
    

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = list(set(banned))
        banned.sort()
        res= 0
        i = 1
        for ban in banned:
            while i <= maxSum and i <= n:
                if i == ban:
                    i += 1
                    break
                else:
                    maxSum -= i
                    res += 1
                    i += 1
            else:
                return res

        while i <= maxSum and i <= n:
            maxSum -= i
            res += 1
            i += 1
        return res  # 59ms

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        set_banned = set(banned)
        for i in range(1,n+1):
            if i > maxSum:
                break
            if i not in set_banned:
                maxSum -= i
                res += 1
        return res  # 46ms

fun = Solution()
banned = [87,193,85,55,14,69,26,133,171,180,4,8,29,121,182,78,157,53,26,7,117,138,57,167,8,103,32,110,15,190,139,16,49,138,68,69,92,89,140,149,107,104,2,135,193,87,21,194,192,9,161,188,73,84,83,31,86,33,138,63,127,73,114,32,66,64,19,175,108,80,176,52,124,94,33,55,130,147,39,76,22,112,113,136,100,134,155,40,170,144,37,43,151,137,82,127,73]
outcome = fun.maxCount(banned,1079,87)
print(outcome)
