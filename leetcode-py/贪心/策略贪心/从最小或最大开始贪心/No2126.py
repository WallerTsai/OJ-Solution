# 难度中等
from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for plant in asteroids:
            if mass >= plant:
                mass += plant
            else:
                return False
        return True