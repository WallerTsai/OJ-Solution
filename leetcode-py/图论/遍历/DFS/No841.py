from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(i:int):
            visited.add(i)
            for key in rooms[i]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)


