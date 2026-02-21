from bisect import bisect_left,bisect_right
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_left(arr,x)
        length = len(arr)
        left,right = index,index+1
        while k:
            if left == 0:
                right += 1
            elif right >= length:
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x :
                    left -= 1
                else:
                    right += 1
            k -= 1
        return arr[left:right-1]  # 错误
            
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_left(arr,x)
        length = len(arr)
        left,right = index,index+1
        while k-1:
            if left == 0:
                right += 1
            elif right >= length:
                left -= 1
            else:
                if x - arr[left-1] <= arr[right] - x :
                    left -= 1
                else:
                    right += 1
            k -= 1
        return arr[left:right]  # 错误 arr[index] 不应该默认是最接近的值

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_left(arr,x)
        length = len(arr)
        right = index
        left = right - 1
        while k:
            if left < 0:
                right += 1
            elif right == length:
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x:
                    left -= 1
                else:
                    right += 1
            k -= 1
        return arr[left+1:right]    # 7ms

class Solution:
    # leetcode 大佬
    # 二分，定长窗口
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 二分法，始终对长度为k的连续子数组进行操作，最终确定起点位置即可，即左端点
        n = len(arr)
        # 最大的起点为n-k，这样才能保证选取长度为k的连续子数组
        left, right = 0, n - k
        while left < right:
            mid = (left + right) // 2
            # mid与mid+k分别为当前的左右端点
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left+k]




