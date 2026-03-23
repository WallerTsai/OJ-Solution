class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        record = dict()

        ans = 0
        for i, ch in enumerate(s):
            # left = -1 if ch not in record else record[ch]
            left = record.get(ch, -1)
            right = n
            ans += (i - left) * (right - i)
            record[ch] = i

        return ans