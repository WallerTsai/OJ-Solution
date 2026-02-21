class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        cnt = flat = 0
        for c1, c2 in zip(s1,s2):
            if c1 > c2:
                cnt += 1
            elif c1 < c2:
                cnt -= 1
            else:
                flat += 1
        
        n = len(s1)
        return (abs(cnt) + flat) == n

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        temp = []
        for c1,c2 in zip(s1,s2):
            if c1 >= c2:
                temp.append(c1)
            else:
                temp.append(c2)
        return temp == s1 or temp == s2

fun = Solution()
fun.checkIfCanBreak("abc","xya")