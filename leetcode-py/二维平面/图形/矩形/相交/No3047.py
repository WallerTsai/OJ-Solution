from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def f(bottomLeft1, topRight1, bottomLeft2, topRight2):
            if bottomLeft1[0] > bottomLeft2[0]:
                bottomLeft1, bottomLeft2 = bottomLeft2, bottomLeft1
                topRight1, topRight2 = topRight2, topRight1

            if topRight1[0] <= bottomLeft2[0]:
                # 右方无交集
                return 0
            
            if topRight1[1] <= bottomLeft2[1]:
                # 上
                return 0
            
            if bottomLeft1[1] >= topRight2[1]:
                # 下
                return 0

            bottomLeft3 = (bottomLeft2[0], max(bottomLeft1[1], bottomLeft2[1]))
            topRight3 = (topRight1[0], min(topRight1[1], topRight2[1]))

            return min((topRight3[0] - bottomLeft3[0]), (topRight3[1] - bottomLeft3[1]))
        
        ans = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i):
                ans = max(ans, f(bottomLeft[j], topRight[j], bottomLeft[i], topRight[i]))

        return pow(ans, 2)  # 错误
    

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def f(bottomLeft1, topRight1, bottomLeft2, topRight2):
            if bottomLeft1[0] > bottomLeft2[0]:
                bottomLeft1, bottomLeft2 = bottomLeft2, bottomLeft1
                topRight1, topRight2 = topRight2, topRight1

            if topRight1[0] <= bottomLeft2[0]:
                # 右方无交集
                return 0
            
            if topRight1[1] <= bottomLeft2[1]:
                # 上
                return 0
            
            if bottomLeft1[1] >= topRight2[1]:
                # 下
                return 0

            bottomLeft3 = (bottomLeft2[0], max(bottomLeft1[1], bottomLeft2[1]))
            topRight3 = (min(topRight1[0], topRight2[0]), min(topRight1[1], topRight2[1]))

            return min((topRight3[0] - bottomLeft3[0]), (topRight3[1] - bottomLeft3[1]))
        
        ans = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i):
                ans = max(ans, f(bottomLeft[j], topRight[j], bottomLeft[i], topRight[i]))

        return pow(ans, 2)  # 2712ms
    

