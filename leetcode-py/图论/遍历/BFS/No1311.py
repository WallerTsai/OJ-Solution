from collections import Counter, deque
from itertools import count
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n  = len(friends)
        q = deque([id])
        visited = [False] * n
        visited[id] = True

        for _ in range(level):
            for _ in range(len(q)):
                u = q.popleft()
                for v in friends[u]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True

        f = Counter()
        while q:
            u = q.popleft()
            for w in watchedVideos[u]:
                f[w] += 1

        videos = sorted((f.items()),key=lambda x: (x[1],x[0]))
        ans = [video[0] for video in videos]

        return ans  # 15ms


