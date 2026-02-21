from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return (n - (1 - flowerbed[0])) <= 0

        # 首：
        if flowerbed[0] == flowerbed[1]:
            flowerbed[0] = 1
            n -= 1

        for i in range(1,len(flowerbed)-2):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
        
        # 尾
        if flowerbed[-1] == flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        
        return n <= 0



