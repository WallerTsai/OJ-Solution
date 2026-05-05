from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt['R'] == cnt['L'] and cnt['U'] == cnt['D']