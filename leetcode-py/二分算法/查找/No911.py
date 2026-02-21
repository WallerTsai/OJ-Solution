from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.person_ = []
        cnt = Counter()
        index_ = defaultdict(list)
        for index in range(len(times)):

            cnt[persons[index]] += 1
            index_[persons[index]].append(index)

            if index < len(times)-1 and times[index+1] == times[index]:
                continue

            if len(cnt) == 1:
                self.person_.append(cnt.most_common(1)[0][0])
                continue

            max_count = max(cnt.values())
            keys_with_max_count = [key for key,count in cnt.most_common() if count == max_count]
            if len(keys_with_max_count) > 1:
                last_index = 0
                for p in keys_with_max_count:
                    last_index = max(last_index,index_[p][-1])
                self.person_.append(persons[last_index])
            else:
                self.person_.append(keys_with_max_count[0])
    def q(self, t: int) -> int:
        index = bisect_right(self.times,t)
        return self.person_[index-1]    # 838ms


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        cnt = defaultdict(int)
        top = None
        self.tops = []
        self.times = times
        for i in range(len(times)):
            cnt[persons[i]] += 1
            if  top is None or cnt[persons[i]] >= cnt[top]:
                top = persons[i]
            self.tops.append(top)

    def q(self, t: int) -> int:
        index = bisect_right(self.times,t)
        return self.tops[index-1]    # 76ms

fun = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
print(fun.person_)

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)