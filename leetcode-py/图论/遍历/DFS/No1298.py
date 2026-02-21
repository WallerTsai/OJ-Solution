from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        open_boxes = []
        get_boxer = []
        ans = 0

        for box in initialBoxes:
            if status[box]:
                open_boxes.append(box)
            else:
                get_boxer.append(box)

        while open_boxes:
            cur_box = open_boxes.pop()
            ans += candies[cur_box]
            
            if not keys[cur_box] and not containedBoxes[cur_box]:
                continue

            for k in keys[cur_box]:
                status[k] = 1
            
            get_boxer.extend(containedBoxes[cur_box])

            nx = []
            for  box in get_boxer:
                if status[box]:
                    open_boxes.append(box)
                else:
                    nx.append(box)
            
            get_boxer = nx

        return ans  # 11ms

f = Solution()

s = [1,0,0,0,0,0]
c = [1,1,1,1,1,1]
k = [[1,2,3,4,5],[],[],[],[],[]]
con = [[1,2,3,4,5],[],[],[],[],[]]
i = [0]


f.maxCandies(s,c,k,con,i)