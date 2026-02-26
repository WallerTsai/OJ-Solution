from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        MX = max(milestones)
        if total - MX >= MX:
            return total
        else:
            return 2 * (total - MX) + 1 # 7ms
        


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        MX = max(milestones)
        return min((total - MX) * 2 + 1, total)
    
    