class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # x x A x x 
        # x x A x
        # x x A 

        #   x A x x 
        #   x A x 
        #   x A 

        #     A x x
        #     A x 
        #     A 

        # 3 * 3 

        n = len(s)
        record = dict()
        pre = [-1] * n
        sub = [n] * n

        for i, ch in enumerate(s):
            if ch in record:
                pre[i] = record[ch]
                sub[record[ch]] = i
            record[ch] = i

        ans = 0
        for i, ch in enumerate(s):
            left = pre[i]
            right = sub[i]
            ans += (i - left) * (right - i)

        return ans
    

class Solution:
    # 灵神
    def uniqueLetterString(self, s: str) -> int:
        ans = total = 0
        last0, last1 = {}, {}
        for i, c in enumerate(s):
            total += i - 2 * last0.get(c, -1) + last1.get(c, -1)
            ans += total
            last1[c] = last0.get(c, -1)
            last0[c] = i
        return ans