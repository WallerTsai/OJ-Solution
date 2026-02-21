from collections import defaultdict, deque
from typing import List
import heapq


import collections
import heapq
import itertools

# 摘自国外lc高赞回答
class Twitter(object):
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        # 注意| {userId} 需要并上自己的推文
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        # 至多取前10项
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)  # 43ms


class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hq = []
        hq.extend(self.tweets[userId])
        for x in self.followees[userId]:
            hq.extend(self.tweets[x])
        hq = list(hq)
        heapq.heapify(hq)
        res = []
        for _ in range(10):
            if not hq:
                break
            _, t = heapq.heappop(hq)
            res.append(t)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)  # 7ms


