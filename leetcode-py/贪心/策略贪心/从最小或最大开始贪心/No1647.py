from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        the_list = sorted(list(counter.values()),reverse=True)
        res = 0
        for i in range(1,len(the_list)):
            if the_list[i] >= the_list[i-1]:
                if the_list[i-1] > 0:    # 0 这种是个特殊情况
                    res += the_list[i] - the_list[i-1] + 1
                    the_list[i] = the_list[i-1] - 1
                else:
                    res += sum(the_list[i:])
                    break
        return res  # 87ms
    
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        nums =sorted(cnt.values(),reverse=True)
        start = sum(nums)
        for i in range(1, len(nums)):
            nums[i] = min(nums[i], nums[i-1]-1)
            if nums[i]<=0: return start-sum(nums[:i])
        return start-sum(nums)  # 75ms
    
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        the_list = sorted(list(counter.values()),reverse=True)
        res = 0
        pre = the_list[0] + 1
        for i in the_list:
            if pre == 0:
                res += i
                continue
            if i >= pre:
                res += i -pre + 1
                pre = pre -1
            else:
                pre = i
            
        return res