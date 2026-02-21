class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = left = 0
        map = {'T':0,'F':0}
        for right,c in enumerate(answerKey):
            map[c] += 1
            while min(map.values()) > k:
                map[answerKey[left]] -= 1
                left += 1
            res = max(res,right-left+1)
        return res  # 322ms
    
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = left = 0
        map = {'T':0,'F':0}
        for right,c in enumerate(answerKey):
            map[c] += 1
            while min(map.values()) > k:
                map[answerKey[left]] -= 1
                left += 1
            res = max(res,right-left+1)
        return res

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        map = {'T':0,'F':0}
        for right,c in enumerate(answerKey):
            map[c] += 1
            if min(map.values()) > k:
                map[answerKey[left]] -= 1
                left += 1
        return right-left+1 # 183ms
    
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        map = {'T':1,'F':0}
        cnt = [0] * 2
        for right,c in enumerate(answerKey):
            cnt[map[c]] += 1
            if min(cnt) > k:
                cnt[map[answerKey[left]]] -= 1
                left += 1
        return right-left+1 # 139ms