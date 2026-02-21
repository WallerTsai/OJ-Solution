from typing import List
from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        length = len(dist)
        if hour < length - 1:
            return -1
        left = 1
        right = max(dist) + 1
        while left < right:
            mid = (right + left) // 2
            count = 0
            for i in dist[:-1]:
                count += (i-1)//mid + 1
            count += dist[-1]/mid
            if count <= hour:
                right = mid
            else:
                left = mid + 1
        if left == max(dist) + 1:
            return -1
        return left # 错误 [1,1,100000] 2.01  ans = 10_000_000

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        length = len(dist)
        if hour <= length - 1:
            return -1
        left = 1
        right = 10**7 + 1   # 这里选题目的区间
        while left < right:
            mid = (right + left) // 2
            count = 0
            for i in dist[:-1]:
                count += (i-1)//mid + 1
            count += dist[-1]/mid
            if count <= hour:
                right = mid
            else:
                left = mid + 1
        if left == max(dist) + 1:
            return -1
        return left # 967ms
    
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # 除了最后一趟列车，前面的每趟列车至少花费 1 小时 ，这里还影响到了最大值取值
        length = len(dist)
        if hour <= length - 1:
            return -1
        left = 1
        right = max(dist) + 1

        if hour <= length:  
            # 这里有个特例，要注意最后一趟车的速度
            # 这里要非常注意精度 只要是关于浮点的乘除
            # 还有就是round()指定小数精度不好用，大多用来四舍五入取整
            return max(right-1,(dist[-1]*100 -1) // (round(hour*100) - (length-1)*100) + 1 )

        while left < right:
            mid = (right + left) // 2
            count = 0
            for i in dist[:-1]:
                count += (i-1)//mid + 1
            count += dist[-1]/mid
            if count <= hour:
                right = mid
            else:
                left = mid + 1
        if left == max(dist) + 1:
            return -1
        return left # 487ms
    # 这里的left和right区间还可以缩小