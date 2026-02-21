class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        return target and (target + self.mechanicalAccumulator(target - 1))
    

class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        return sum(range(target+1))