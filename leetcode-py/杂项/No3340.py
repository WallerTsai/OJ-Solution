class Solution:
    def isBalanced(self, num: str) -> bool:
        ans = [0,0]
        i = 0
        for s in num:
            ans[i] += int(s)
            i = (i + 1) % 2
        return ans[0] == ans[1] # 反复调用int() 浪费时间

class Solution:
    def isBalanced(self, num: str) -> bool:
        a = list(map(int, num))
        return sum(a[::2]) == sum(a[1::2])
    
class Solution:
    def isBalanced(self, num: str) -> bool:
        even = [ord(i) - 48 for i in list(num[0::2])]
        odd = [ord(i) - 48 for i in list(num[1::2])]
        return sum(even) == sum(odd)