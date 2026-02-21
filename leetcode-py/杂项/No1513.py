class Solution:
    MOD = 10 ** 9 + 7
    def numSub(self, s: str) -> int:
        ans = pre = 0
        for ch in s:
            if ch == "1":
                pre += 1
                ans += pre
            else:
                pre = 0
        return ans % self.MOD
    
class Solution:
    def numSub(self, s: str) -> int:
        return (sum(len(s1) * (len(s1) + 1) for s1 in s.split('0')) >> 1) % 1000000007