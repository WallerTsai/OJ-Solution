class Solution:
    def minimumLength(self, s: str) -> int:
        c = ''
        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                c = s[left]
            else:
                break

            while left < right and s[left] == c:
                left += 1
            while left < right and s[right] == c:
                right -= 1

        if left > 0 and s[left-1]==s[right]:
            return 0
        return right - left + 1 # 27ms
    
class Solution:
    # leetcode 大佬
    def minimumLength(self, s: str) -> int:
        left = 0 
        right = len(s)-1
        res =0 
        
        while left<right:
            if s[left]==s[right]:
                pre = s[left]
            else:
                break 
            # left 
            while s[left]==pre and left<right:
                left +=1
            while s[right]==pre and left<=right:
                right -=1
        res = right-left+1
        return res 


                