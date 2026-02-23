from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n = len(players)
        i = 0
        for t in trainers:
            if t >= players[i]:
                i += 1
                if i == n:
                    break
        return i


