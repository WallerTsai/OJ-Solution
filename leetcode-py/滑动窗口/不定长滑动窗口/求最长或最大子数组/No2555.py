from collections import defaultdict
from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        
        cnt = defaultdict(int)
        for n in prizePositions:
            cnt[n] += 1

        left = count1 = temp = m =0
        for right,value in cnt.items():
            temp += value
            while right - left > k:
                if left in cnt:
                    temp -= cnt[left]
                left += 1
            if temp > count1:
                count1 = temp
                m = right
            
        for n in range(m-k,m+1):
            if n in cnt:
                cnt.pop(n)

        left = count2 = temp = 0
        for right,value in cnt.items():
            temp += value
            while right - left > k:
                if left in cnt:
                    temp -= cnt[left]
                left += 1
            if temp > count2:
                count2 = temp
                m = right
        
        return count1 + count2 # 超时

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        
        cnt = defaultdict(int)
        for n in prizePositions:
            cnt[n] += 1
        iter1 = list(cnt.items())
        length1 = len(iter1)
        left = count1 = temp = m =0
        for right in range(length1):
            temp += iter1[right][1]
            while iter1[right][0] - iter1[left][0] > k:
                temp -= iter1[left][1]
                left += 1
            if temp > count1:
                count1 = temp
                m = iter1[right][0]
            
        for n in range(m-k,m+1):
            if n in cnt:
                cnt.pop(n)

        iter2 = list(cnt.items())
        length2 = len(iter2)
        left = count2 = temp = 0
        for right in range(length2):
            temp += iter2[right][1]
            while iter2[right][0] - iter2[left][0] > k:
                temp -= iter2[left][1]
                left += 1
            if temp > count2:
                count2 = temp
        
        return count1 + count2  # 错误且超时
    

class Solution:
    # 灵神
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        length = len(prizePositions)
        if k * 2 + 1 >= prizePositions[-1] - prizePositions[0]:
            return length
        ans = left = 0
        mx = [0] * (length + 1)
        for right,num in enumerate(prizePositions):
            while num - prizePositions[left] > k:
                left += 1
            ans = max(ans,mx[left] + right-left+1)
            mx[right+1] = max(mx[right],right-left+1)
        return ans  # 35ms


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        
        cnt = defaultdict(int)
        for n in prizePositions:
            cnt[n] += 1
        iter = list(cnt.items())
        length = len(iter)
        left = ans = temp = 0
        mx = [0] * (length + 1)
        for right in range(length):
            temp += iter[right][1]
            while iter[right][0] - iter[left][0] > k:
                temp -= iter[left][1]
                left += 1
            ans = max(ans,mx[left] + temp)
            mx[right+1] = max(mx[right],temp)
            
        return ans  # 98ms
