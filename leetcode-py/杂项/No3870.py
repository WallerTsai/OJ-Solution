class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0
        return (n - 1_000 + 1)