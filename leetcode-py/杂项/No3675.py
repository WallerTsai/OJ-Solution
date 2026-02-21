class Solution:
    def minOperations(self, s: str) -> int:
        record = [0] * 26
        for ch in s:
            record[ord(ch) - ord('a')] += 1
        
        ans = to_next = 0
        for i, n in enumerate(record):
            if i == 0:
                continue
            if n:
                to_next = 1
            ans += to_next

        return ans