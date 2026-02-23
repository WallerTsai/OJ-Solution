from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x : (-x[0], x[1]))
        ans = []
        count = 0
        for x, y in people:
            if y < count:
                ans.insert(y,[x,y])
            else:
                ans.append([x,y])
            count += 1
        return ans
