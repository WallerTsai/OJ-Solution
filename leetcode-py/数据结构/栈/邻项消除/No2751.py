from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        di = {x: i for i, x in enumerate(positions)}
        li = []
        for x in sorted(di.keys()):
            i = di[x]
            health = healths[i]
            direction = directions[i]
            while li and direction == 'L' and directions[li[-1]] == 'R':
                idx = li[-1]
                if healths[idx] > health:
                    healths[idx] -= 1
                    health = 0
                    break
                elif healths[idx] == health:
                    healths[idx] = 0
                    li.pop()
                    health = 0
                    break
                else:
                    healths[idx] = 0
                    li.pop()
                    health -= 1

            healths[i] = health
            if health == 0:
                continue
            li.append(i)

        return [h for h in healths if h > 0]
        



class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sorted_indices = sorted(range(len(positions)), key=lambda i: positions[i])

        li = []
        for i in sorted_indices:
            direction = directions[i]
            
            if direction == 'L':
                while li and directions[li[-1]] == 'R':
                    prev_idx = li[-1]
                    if healths[prev_idx] > healths[i]:
                        healths[prev_idx] -= 1
                        healths[i] = 0
                        break
                    elif healths[prev_idx] < healths[i]:
                        healths[i] -= 1
                        healths[prev_idx] = 0
                        li.pop()
                    else:
                        healths[i] = 0
                        healths[prev_idx] = 0
                        li.pop()
                        break
            
            if healths[i] > 0:
                li.append(i)

        return [h for h in healths if h > 0]