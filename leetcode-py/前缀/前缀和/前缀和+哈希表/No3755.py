from collections import defaultdict
from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        lenght = 0
        even = odd = 0
        _xor = 0
        
        cnt = defaultdict(list)
        cnt[0].append((-1, 0, 0))
        for i, num in enumerate(nums):
            
            if num % 2:
                odd += 1
            else:
                even += 1

            _xor ^= num
            if cnt[_xor]:
                for idx, x, y in cnt[_xor]:
                    if even - x == odd - y:
                        if i - idx + 1 > lenght:
                            lenght = i - idx
                            break
            cnt[_xor].append((i, even, odd))

        return lenght   # 超时
    

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        lenght = 0
        even = odd = 0
        _xor = 0
        
        cnt = defaultdict(list)
        cnt[0].append((-1, 0, 0))
        for i, num in enumerate(nums):
            
            if num % 2:
                odd += 1
            else:
                even += 1

            _xor ^= num
            if cnt[_xor]:
                for idx, x, y in cnt[_xor]:
                    if even - x == odd - y:
                        if i - idx + 1 > lenght:
                            lenght = i - idx
                            break
            cnt[_xor].append((i, even, odd))

        return lenght   # 超时
    
    
class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        cnt = defaultdict(int)
        cnt[(0, 0)] = -1
        _xor = temp = 0

        for i, num in enumerate(nums):
            if num % 2 == 0:
                temp += 1
            else:
                temp -= 1

            _xor ^= num
            if (_xor, temp) in cnt:
                ans = max(ans, i - cnt[(_xor, temp)])
            else:
                cnt[(_xor, temp)] = i
        
        return ans 

        

    
fun = Solution()
fun.maxBalancedSubarray([3,1,3,2,0])