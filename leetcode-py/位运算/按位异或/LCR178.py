from typing import List

# 同 No137
class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        aset1 = set()
        aset2 = set()
        for x in actions:
            if x in aset2:
                continue
            elif x in aset1:
                aset1.discard(x)
                aset2.add(x)
            else:
                aset1.add(x)
        return aset1.pop()
    