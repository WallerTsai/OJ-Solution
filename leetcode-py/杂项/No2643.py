from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = cnt = 0
        for i in range(len(mat)):
            cnt2 = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    cnt2 += 1
            if cnt2 > cnt:
                ans = i
                cnt = cnt2
        return [ans,cnt]

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = cnt = 0
        for i, arr in enumerate(mat):
            total1 = sum(arr)
            if total1 > cnt:
                ans = i
                cnt = total1
        return [ans, cnt]
