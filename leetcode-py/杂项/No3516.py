class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) > abs(y - z):
            return 2
        elif abs(x - z) == abs(y - z):
            return 0
        return 1
    
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x - z), abs(y - z)
        return [0, 2, 1][(d1 > d2) - (d1 < d2)]