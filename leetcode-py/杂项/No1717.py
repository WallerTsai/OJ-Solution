class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s += '#'
        cnt_a = cnt_b = ans = 0
        for ch in s:
            if ch == 'a':
                if y >= x and cnt_b > 0:
                    ans += y
                    cnt_b -= 1
                else:
                    cnt_a += 1
            elif ch == 'b':
                if x > y and cnt_a > 0:
                    ans += x
                    cnt_a -= 1
                else:
                    cnt_b += 1
            else:
                ans += min(x, y) * min(cnt_a, cnt_b)
                cnt_a = cnt_b = 0
        return ans