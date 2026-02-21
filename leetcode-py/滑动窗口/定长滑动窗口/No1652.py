from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        length = len(code)
        res = [0] * length

        if k == 0:
            return res
        
        flag = 1
        if k < 0:
            flag = -1
            k = -k

        for i in range(length):
            j = i
            for _ in range(k):
                j = (j + flag + length) % length
                res[i] += code[j]
        
        return res  # 11ms 复杂度O(nk)

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        length = len(code)
        res = [0] * length

        if k == 0:
            return res
        
        
        res[0] = sum(code[1:k+1]) if k > 0 else sum(code[k:])

        flag = 1
        if k < 0:
            flag = -1

        i = 0
        for _ in range(length-1):
            i = (i + flag + length) % length
            res[i] = res[(i-flag) % length] - code[i] + code[(i+k+length)%length]
        
        return res  # 0ms

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if length == 0 or k == 0:
            return [0] * length

        res = [0] * length
        res[0] = sum(code[:k+1]) if k > 0 else sum(code[k:])

        flag = step = 1 if k > 0 else -1
        k = abs(k)

        for i in range(1, length):
            res[i] = res[i - step] - flag * code[i] + flag * code[(i + k) % length]

        return res



