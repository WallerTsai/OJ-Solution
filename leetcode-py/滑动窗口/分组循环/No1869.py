class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ch = '0'
        l = 0
        n = len(s)
        i = 0
        while i < n:
            x = s[i]
            start = i
            i += 1
            while i < n and s[i] == x:
                i += 1
            if x == '0':
                if i - start >= l:
                    ch = '0'
                    l = i - start
            else:
                if i - start > l:
                    ch = '1'
                    l = i - start
        return False if ch == '0' else True
