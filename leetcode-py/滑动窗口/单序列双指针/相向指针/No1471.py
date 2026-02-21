from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        mid = sorted(arr)[(len(arr)-1)//2]
        res = sorted(arr,key= lambda x:(abs(x-mid),x),reverse=True)
        return res[:k]  # 307ms

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res,length = [],len(arr)
        arr.sort()
        mid = arr[(length-1)//2]
        left,right = 0,len(arr)-1
        while k > 0:
            if arr[right]-mid >= mid - arr[left]:
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left +=1
            k -= 1
        return res  # 90ms
