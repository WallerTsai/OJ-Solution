from bisect import bisect_right
from typing import List

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        res = 0
        for i in staple:
            for j in drinks:
                if i + j <= x:
                    res +=1
                else:
                    break
            if i >= x:
                break
        return res  # 我滴乖乖居然超时了
    
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        res = 0
        for i in staple:
            if i >= x:
                break
            number = bisect_right(drinks,x-i)
            res += number
        return res  # 348ms
    
class Solution:
    # leetcode 最快
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        ans = 0
        arr = [0 for i in range(x+1)]
        
        for sta in staple:
            if sta < x:
                arr[sta] += 1
        
        for i in range(2, x):
            arr[i] += arr[i-1]
        
        for drink in drinks:
            lt = x - drink
            if lt <= 0:
                continue
            ans += arr[lt]
            
        return ans % (10 ** 9 + 7)