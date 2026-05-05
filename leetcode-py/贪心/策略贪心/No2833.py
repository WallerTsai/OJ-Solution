class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        r = moves.count("R")
        l = moves.count("L")
        return abs(r - l) + n - r - l